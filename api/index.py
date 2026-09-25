import os
import json
import urllib.request
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client, Client
from langchain_groq import ChatGroq
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def read_root():
    return FileResponse("index.html")

class QueryRequest(BaseModel):
    query: str

def get_hf_embedding(text: str, hf_token: str):
    url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"
    headers = {
        "Authorization": f"Bearer {hf_token}",
        "Content-Type": "application/json"
    }
    data = json.dumps({"inputs": text}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as response:
        result = json.loads(response.read().decode())
        return result[0] if isinstance(result[0], list) else result

@app.post("/api/chat")
def chat(request: QueryRequest):
    query = request.query
    
    hf_token = os.environ.get("HF_TOKEN")
    if not hf_token:
        return {"answer": "Error: HF_TOKEN environment variable is missing. Please add it to your Vercel project."}
        
    try:
        query_embedding = get_hf_embedding(query, hf_token)
    except Exception as e:
        return {"answer": f"Failed to generate embeddings via direct API: {str(e)}"}
        
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
