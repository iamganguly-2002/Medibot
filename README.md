🩺 Medibot – AI-Powered Medical Chatbot
Medibot is an AI-powered medical chatbot designed to assist users by answering health-related queries. It combines the power of Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs) to provide context-aware, reliable responses. The system integrates a FAISS vector database for semantic search and is deployed using Streamlit for a user-friendly interface.

🚀 Features
✅ RAG-based Pipeline: Combines local medical knowledge with LLMs for accurate responses.

✅ FAISS Vector Store: Efficient semantic search over medical documents.

✅ Mistral LLM (Hugging Face): Generates natural, context-aware answers.

✅ Streamlit UI: An interactive web interface for chatting with Medibot.

✅ Secure API Handling: Utilizes .env files for managing sensitive keys (Hugging Face token, etc.).

📂 Project Structure
.
├── vectorstore/               # Stores FAISS vector database
├── connect_memory_with_llm.py   # Python script for RAG + LLM integration
├── app.py                     # Main Streamlit application
├── requirements.txt           # Project dependencies
├── .env                       # Environment variables (API keys)
└── README.md                  # Project documentation

⚙️ Installation
Clone the repository:

git clone https://github.com/iamganguly-2002/Medibot.git
cd Medibot

Create and activate a virtual environment:

On Linux/macOS:

python -m venv .venv
source .venv/bin/activate

On Windows:

python -m venv .venv
.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Add your Hugging Face API key:
Create a new file named .env in the root directory of the project and add your token:

HUGGINGFACEHUB_API_TOKEN=your_token_here

Run the App:

streamlit run app.py

Open the browser at http://localhost:8501 to interact with Medibot.

🧠 Tech Stack
Python: 3.10+

Streamlit: Frontend framework for the web interface.

LangChain: Framework for building the RAG pipeline.

FAISS: Vector database for semantic search.

Hugging Face: Utilized for the Mistral LLM.

📌 Keywords
Retrieval-Augmented Generation (RAG)

Medical Chatbot

Large Language Model (LLM)

FAISS Vector Store

Streamlit

🔮 Future Scope
Multilingual Support: Implement support for multiple languages to serve a wider user base.

Speech-to-Text Integration: Allow users to interact with the chatbot using voice commands.

Real Doctor Integration: Integrate with a database or API of certified doctors for more specific and personalized consultations.

📸 Screenshots
Add screenshots of your Streamlit app here to showcase its user interface and functionality.

👨‍🏫 Faculty Guide
Br. Tamal Maharaj

👉 GitHub Repository
https://github.com/iamganguly-2002/Medibot
