import os
import sys
import argparse
import warnings
from dotenv import load_dotenv

# Suppress HuggingFace and deprecation warnings
warnings.filterwarnings("ignore")
os.environ["TOKENIZERS_PARALLELISM"] = "false"
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

if not SUPABASE_URL or not SUPABASE_KEY or not GROQ_API_KEY:
    raise ValueError("Missing Supabase or Groq credentials in .env")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0.2)

# Set TOP_K default to 10 as requested
DEFAULT_TOP_K = 10

def get_relevant_chunks(query: str, match_count: int = DEFAULT_TOP_K):
    """Fetch the most relevant document chunks from Supabase."""
    query_embedding = embeddings.embed_query(query)
    
    response = supabase.rpc(
        "match_documents",
        {
            "query_embedding": query_embedding,
            "match_count": match_count
        }
    ).execute()
    
    return response.data

def synthesize_answer(query: str, chunks: list):
    """Use the LLM to generate an answer based ONLY on the retrieved chunks."""
    
    if not chunks:
        return "No relevant information found in the knowledge base."
        
    context_parts = []
    for chunk in chunks:
        machine_name = chunk.get("metadata", {}).get("machine_name", "Unknown")
        content = chunk.get("content", "")
        # Include metadata inline so the LLM can see the machine name
        context_parts.append(f"---\n[Machine: {machine_name}]\n{content}\n---")
        
    context_string = "\n\n".join(context_parts)
    
    system_prompt = (
        "You are an expert offensive security assistant. You answer questions strictly based on the provided "
        "Hack The Box (HTB) write-up chunks. \n"
        "Follow these rules strictly:\n"
        "1. Answer ONLY using the provided context chunks. Do NOT hallucinate or use external knowledge.\n"
        "2. Group techniques logically (e.g., SAM/SYSTEM hive dumps, potato-family exploits).\n"
        "3. Provide a short, concise explanation for each technique.\n"
        "4. CRUCIAL: Explicitly cite the machine name that demonstrates the technique at the end of each bullet point "
        "using the EXACT format: `(seen on: [Machine Name])`. Extract this from the `[Machine: <name>]` tag above each context block.\n"
        "If the context does not contain the answer, simply state that you don't have enough information based on the provided notes."
    )
    
    user_prompt = f"Context:\n{context_parts}\n\nQuery: {query}"
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]
    
    response = llm.invoke(messages)
    return response.content

def main():
    parser = argparse.ArgumentParser(description="Query the HTB Wiki RAG pipeline.")
    parser.add_argument("query", type=str, help="The natural language query to ask (e.g., 'Windows privilege escalation cheatsheet')")
    parser.add_argument("--top-k", type=int, default=DEFAULT_TOP_K, help=f"Number of chunks to retrieve (default: {DEFAULT_TOP_K})")
    
    args = parser.parse_args()
    
    print(f"\nRetrieving top {args.top_k} chunks for query: '{args.query}'...\n")
    chunks = get_relevant_chunks(args.query, match_count=args.top_k)
    
    print("Synthesizing answer...\n")
    answer = synthesize_answer(args.query, chunks)
    
    # Safely handle Windows console encoding issues for special characters (like non-breaking hyphens)
    safe_answer = answer.encode(sys.stdout.encoding or 'utf-8', errors='replace').decode(sys.stdout.encoding or 'utf-8')
    
    print("="*10)
    print("ANSWER:")
    print()
    print(safe_answer)
    print("="*10)

if __name__ == "__main__":
    main()
