import os
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client, Client
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from fastapi.responses import FileResponse

app = FastAPI()

# Serve the HTML frontend locally
@app.get("/")
def read_root():
    return FileResponse("index.html")

class QueryRequest(BaseModel):
    query: str

@app.post("/api/chat")
def chat(request: QueryRequest):
    query = request.query
    
    # 1. We must use the HF API Embeddings on Vercel to bypass the 250MB limit
    hf_token = os.environ.get("HF_TOKEN")
    if not hf_token:
        return {"answer": "Error: HF_TOKEN environment variable is missing. Please add it to your Vercel project."}
        
    embeddings = HuggingFaceInferenceAPIEmbeddings(
        api_key=hf_token,
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    try:
        query_embedding = embeddings.embed_query(query)
    except Exception as e:
        return {"answer": f"Failed to generate embeddings: {str(e)}"}
        
    # 2. Search Supabase
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    
    response = supabase.rpc("match_documents", {"query_embedding": query_embedding, "match_count": 10}).execute()
    chunks = []
    for chunk in response.data:
        machine = chunk.get("metadata", {}).get("machine_name", "Unknown")
        content = chunk.get("content", "")
        chunks.append(f"Machine: {machine}\nContent: {content}\n")
    
    context = "\n---\n".join(chunks)
    if not chunks:
        return {"answer": "No relevant context found in the database for this question."}
        
    # 3. Synthesize via Groq
    llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0.2)
    prompt = f"""You are a helpful cybersecurity AI assistant parsing HackTheBox writeups. 
    Answer the user's question based ONLY on the provided context.
    If the context doesn't contain the answer, say "I don't have enough information".
    For each fact you use, append '(seen on: [Machine])' to the end of the sentence or bullet point.
    
    Context:
    {context}
    
    Question: {query}
    
    Answer clearly in Markdown format. Do NOT hallucinate.
    """
    
    try:
        msg = llm.invoke(prompt)
        return {"answer": msg.content}
    except Exception as e:
        return {"answer": f"Failed to generate answer from Groq: {str(e)}"}
