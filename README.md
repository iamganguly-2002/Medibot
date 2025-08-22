🩺 Medibot – AI-Powered Medical Chatbot

Medibot is an AI-powered medical chatbot designed to assist users by answering health-related queries. It combines the power of Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs) to provide context-aware, reliable responses. The system integrates a FAISS vector database for semantic search and is deployed using Streamlit for a user-friendly interface.

🚀 Features

✅ RAG-based Pipeline – combines local medical knowledge with LLMs for accurate responses

✅ FAISS Vector Store – efficient semantic search over medical documents

✅ Mistral LLM (Hugging Face) – generates natural, context-aware answers

✅ Streamlit UI – interactive web interface for chatting with Medibot

✅ Secure API Handling – .env for sensitive keys (Hugging Face token, etc.)

📂 Project Structure
📦 MEDICAL-CHATBOT
 ┣ 📂 vectorstore/          # Stores FAISS database  
 ┣ 📜 connect_memory_with_llm.py   # RAG + LLM integration  
 ┣ 📜 app.py                # Streamlit app (main UI)  
 ┣ 📜 requirements.txt      # Project dependencies  
 ┣ 📜 .env                  # Environment variables (API keys)  
 ┣ 📜 README.md             # Project documentation  

⚙️ Installation

1. Clone the repository:

  git clone https://github.com/iamganguly-2002/Medibot.git
  cd Medibot


2. Create and activate a virtual environment:

   python -m venv .venv
   source .venv/bin/activate   # On Linux/Mac
.    venv\Scripts\activate      # On Windows


3. Install dependencies:

    pip install -r requirements.txt


4. Add your Hugging Face API key in a .env file:

    HUGGINGFACEHUB_API_TOKEN=your_token_here

▶️ Run the App
    streamlit run app.py


Open the browser at http://localhost:8501 to interact with Medibot.

🧠 Tech Stack

    Python 3.10+

    Streamlit (Frontend)

    LangChain (RAG Pipeline)

    FAISS (Vector DB)

    Hugging Face Mistral Model

📌 Keywords

    Retrieval-Augmented Generation (RAG)

    Medical Chatbot

    Large Language Model (LLM)

    FAISS Vector Store

    Streamlit

