<div align="center">
  <h1>🛡️ HackTheBox Wiki RAG Pipeline</h1>
  <p><i>An AI-powered Retrieval-Augmented Generation (RAG) system for cybersecurity writeups.</i></p>
</div>

---

## 🚀 Overview
This repository contains a full RAG pipeline designed to intelligently parse, embed, search, and synthesize answers from HackTheBox (HTB) penetration testing writeups. 

### 🏗️ Architecture
- **Web App:** Next-gen Claude-style chat UI hosted on Vercel (`index.html` + `api/index.py`).
- **Embeddings:** HuggingFace Inference API (`sentence-transformers/all-MiniLM-L6-v2`) via LangChain.
- **Vector Database:** Cloud-hosted Supabase with `pgvector`.
- **LLM Synthesis:** Groq (`openai/gpt-oss-20b`).

---

## 🌐 Live Web Demo (For Quick Evaluation)
If you do not want to run the code locally, you can evaluate the RAG pipeline directly from your browser! 

👉 **[Click Here to open the Vercel App](https://your-app-name.vercel.app)** 

*Note for HR: The web app connects directly to the cloud Supabase database and Groq. Just paste any of the 15 questions from the test set below into the chat box!*

---

## 💻 How to Run Locally (Reviewer Guide)

To make evaluation as frictionless as possible, the Supabase database is **already fully populated** with the vectorized document chunks. You do not need to run the ingestion script, wait for embeddings to process, or set up your own database.

### Step 1: Clone & Setup
Clone the repository and install the dependencies:
```bash
git clone https://github.com/your-username/htb-wiki.git
cd htb-wiki
python -m venv venv
venv\Scripts\activate      # On Windows
# source venv/bin/activate # On Linux/Mac
pip install -r requirements.txt
```

### Step 2: Configure Environment
Create a `.env` file in the root directory. Add the API keys (provided to you securely outside of this repository) to connect to the pre-populated database:
```env
SUPABASE_URL=your_provided_url
SUPABASE_KEY=your_provided_key
GROQ_API_KEY=your_provided_key
```

### Step 3: Run a Query
You can now ask the RAG pipeline a question. It will reach out to the cloud database, retrieve the top 10 most relevant context chunks, and synthesize a clean markdown answer with citations.
```bash
python query.py "Which machine has no modifiable services identified by winPEAS?"
```

---

## 🧪 Test Question Set
The pipeline has been tuned to handle both broad "cheatsheet" style requests and highly targeted factual queries, as well as resisting hallucinations for "trick" questions. Try running any of these 15 test questions through `query.py`:

1. Give me a cheatsheet of all Windows privileges abused for escalation across these machines.
2. Give me a cheatsheet of the initial access and foothold vectors across these machines.
3. What port does the Hector service run on?
4. How was injection used to gain a shell?
5. How is SeLoadDriverPrivilege abused to get SYSTEM on the Fuse machine?
6. Which machine has no modifiable services identified by winPEAS?
7. What tool or technique is typically used to abuse SeImpersonatePrivilege on machines like Conceal?
8. Which machine has SeSecurityPrivilege, SeTakeOwnershipPrivilege and SeIncreaseQuotaPrivilege disabled by default?
9. What credentials are provided for initial access on the Administrator machine?
10. What service runs on TCP port and what critical information does it reveal?
11. Which machines have SeMachineAccountPrivilege enabled?
12. How do you back up protected files using SeBackupPrivilege on Freelancer?
13. How is SeIncreaseBasePriorityPrivilege increase scheduling priority?
14. What local privilege escalation exploit is MS14-040 associated with?
15. How are passwords or hashes extracted from the database on Blockblock and Checker?

---

## 📊 Evaluation & Design Note
Please read the attached `evaluation_writeup.md` for a comprehensive breakdown of the pipeline's performance. It includes:
* Precision and Recall scoring for all 15 test questions based on a hand-derived ground truth.
* Qualitative notes on hallucination prevention and citation accuracy.
* A brief design note justifying the Markdown chunking strategy and embedding-based retrieval model.
