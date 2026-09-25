import logging
import os
import re
from collections import defaultdict

import requests
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from pydantic import BaseModel
from supabase import Client, create_client

load_dotenv()

app = FastAPI()
logger = logging.getLogger(__name__)

HF_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
HF_INFERENCE_URL = (
    "https://router.huggingface.co/hf-inference/models/"
    f"{HF_MODEL}/pipeline/feature-extraction"
)
EMBEDDING_DIMENSIONS = 384
DEFAULT_TOP_K = 10

ANSWER_SYSTEM_PROMPT = """You are a helpful cybersecurity AI assistant parsing
HackTheBox writeups. Answer only from the supplied context. If the context does
not contain the answer, say "I don't have enough information".

Follow these response rules strictly:
1. Never output a Markdown table or use pipes to create tabular rows.
2. Use short headings followed by concise paragraphs or bullet points.
3. Put commands and code snippets in fenced code blocks on their own lines.
4. Cite facts as '(seen on: <machine name>)', for example '(seen on: Control)'.
   Use only the machine name from the context tag; do not include the word
   'Machine' inside the citation.
5. Keep the answer focused and do not repeat the conclusion.
"""

STOP_WORDS = {
    "about",
    "after",
    "also",
    "been",
    "find",
    "found",
    "does",
    "from",
    "have",
    "has",
    "how",
    "identified",
    "into",
    "machine",
    "than",
    "that",
    "their",
    "these",
    "this",
    "using",
    "what",
    "when",
    "where",
    "which",
    "with",
}


@app.get("/")
def read_root():
    return FileResponse("index.html")


class QueryRequest(BaseModel):
    query: str


def _extract_embedding(result):
    """Return one 384-value sentence embedding from the HF response."""
    while (
        isinstance(result, list)
        and len(result) == 1
        and isinstance(result[0], list)
    ):
        result = result[0]

    if not isinstance(result, list):
        raise ValueError("Hugging Face returned an invalid embedding payload")

    if len(result) != EMBEDDING_DIMENSIONS or not all(
        isinstance(value, (int, float)) for value in result
    ):
        raise ValueError(
            f"Hugging Face returned an embedding with an unexpected shape; "
            f"expected {EMBEDDING_DIMENSIONS} values"
        )

    return result


def get_hf_embedding(text: str, hf_token: str):
    """Generate a query vector through Hugging Face's current router API."""
    response = requests.post(
        HF_INFERENCE_URL,
        headers={
            "Authorization": f"Bearer {hf_token}",
            "Content-Type": "application/json",
        },
        json={"inputs": text},
        timeout=(5, 20),
    )
    response.raise_for_status()
    return _extract_embedding(response.json())


def _search_terms(query: str, maximum: int = 5):
    words = re.findall(r"[a-z0-9][a-z0-9_.-]{2,}", query.lower())
    unique_words = list(dict.fromkeys(words))
    useful_words = [word for word in unique_words if word not in STOP_WORDS]
    return sorted(useful_words, key=len, reverse=True)[:maximum]


def get_lexical_chunks(supabase: Client, query: str, match_count: int):
    """Retrieve likely chunks without embeddings when HF is unavailable."""
    terms = _search_terms(query)
    if not terms:
        return []

    chunks_by_id = {}
    scores = defaultdict(float)

    for term in terms:
        response = (
            supabase.table("documents")
            .select("id,content,metadata")
            .ilike("content", f"%{term}%")
            .limit(20)
            .execute()
        )
        for chunk in response.data or []:
            chunk_id = str(chunk.get("id", ""))
            if not chunk_id:
                continue
            chunks_by_id[chunk_id] = chunk
            scores[chunk_id] += 1 + (len(term) / 20)

    ranked_ids = sorted(scores, key=scores.get, reverse=True)
    return [chunks_by_id[chunk_id] for chunk_id in ranked_ids[:match_count]]


def get_relevant_chunks(
    supabase: Client, query: str, hf_token: str, match_count: int = DEFAULT_TOP_K
):
    if not hf_token:
        logger.warning("HF_TOKEN is missing; using Supabase lexical fallback")
        return get_lexical_chunks(supabase, query, match_count)

    try:
        query_embedding = get_hf_embedding(query, hf_token)
        response = supabase.rpc(
            "match_documents",
            {"query_embedding": query_embedding, "match_count": match_count},
        ).execute()
        return response.data or []
    except (requests.RequestException, ValueError, KeyError, IndexError):
        logger.exception(
            "Embedding retrieval failed; using Supabase lexical fallback"
        )
        return get_lexical_chunks(supabase, query, match_count)


@app.post("/api/chat")
def chat(request: QueryRequest):
    query = request.query.strip()
    if not query:
        return {"answer": "Please enter a question."}

    hf_token = os.environ.get("HF_TOKEN")
    supabase_url = os.environ.get("SUPABASE_URL")
    supabase_key = os.environ.get("SUPABASE_KEY")
    groq_api_key = os.environ.get("GROQ_API_KEY")
    if not all((supabase_url, supabase_key, groq_api_key)):
        logger.error("One or more required API environment variables are missing")
        return {
            "answer": "The service is not fully configured. Please contact the site owner."
        }

    try:
        supabase: Client = create_client(supabase_url, supabase_key)
        retrieved_chunks = get_relevant_chunks(supabase, query, hf_token)
    except Exception:
        logger.exception("Document retrieval failed")
        return {
            "answer": "I couldn't search the knowledge base right now. Please try again shortly."
        }

    if not retrieved_chunks:
        return {"answer": "No relevant context found in the database for this question."}

    context_parts = []
    for chunk in retrieved_chunks:
        machine = chunk.get("metadata", {}).get("machine_name", "Unknown")
        content = chunk.get("content", "")
        context_parts.append(f"[Machine: {machine}]\n{content}")
    context = "\n\n---\n\n".join(context_parts)

    llm = ChatGroq(
        api_key=groq_api_key,
        model="openai/gpt-oss-20b",
        temperature=0.2,
    )
    user_prompt = f"""Context:
{context}

Question: {query}
"""

    try:
        message = llm.invoke(
            [
                SystemMessage(content=ANSWER_SYSTEM_PROMPT),
                HumanMessage(content=user_prompt),
            ]
        )
        return {"answer": message.content}
    except Exception:
        logger.exception("Groq answer generation failed")
        return {
            "answer": "I found relevant notes but couldn't generate an answer right now. "
            "Please try again shortly."
        }
