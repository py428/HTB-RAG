import os
from dotenv import load_dotenv
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing Supabase credentials in .env")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def extract_machine_name(filename):
    """Example: htb-absolute.md -> Absolute"""
    basename = os.path.basename(filename)
    name = basename.replace('htb-', '').replace('.md', '')
    return name.title()

def clear_database():
    print("Clearing existing documents from the database...")
    try:
        supabase.rpc("truncate_documents", {}).execute()
        print("Database cleared successfully.")
    except Exception as e:
        print(f"Error clearing database: {e}")
        print("Trying fallback delete method...")
        try:
            # Fallback if RPC isn't set up
            supabase.table("documents").delete().neq("id", "00000000-0000-0000-0000-000000000000").execute()
            print("Database cleared using fallback method.")
        except Exception as e_fallback:
            print(f"Fallback delete failed: {e_fallback}")

def main():
    clear_database()

    raw_dir = "raw"
    if not os.path.exists(raw_dir):
        print(f"Directory '{raw_dir}' does not exist.")
        return

    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)

    for filename in os.listdir(raw_dir):
        if not filename.endswith(".md"):
            continue
        
        filepath = os.path.join(raw_dir, filename)
        machine_name = extract_machine_name(filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if not content.strip():
            continue
        
        # Split by markdown headers
        md_docs = markdown_splitter.split_text(content)
        
        # Further split by characters if chunks are too long
        chunks = text_splitter.split_documents(md_docs)
        
        if not chunks:
            continue
            
        print(f"Processing {machine_name}: {len(chunks)} chunks")
        
        # Batch embed all chunks for this machine locally
        texts = [chunk.page_content for chunk in chunks]
        
        # Local embeddings - no rate limits!
        doc_embeddings = embeddings.embed_documents(texts)
            
        # Prepare for Supabase
        records = []
        for i, chunk in enumerate(chunks):
            metadata = chunk.metadata
            metadata["machine_name"] = machine_name
            
            records.append({
                "content": chunk.page_content,
                "metadata": metadata,
                "embedding": doc_embeddings[i]
            })
            
            # Batch insert to avoid huge requests (batch size 64)
            if len(records) >= 64:
                supabase.table("documents").insert(records).execute()
                records = []
                
        # Insert remaining
        if records:
            supabase.table("documents").insert(records).execute()

    print("Ingestion complete.")

if __name__ == "__main__":
    main()
