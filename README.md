**🩺 Medibot – AI-Powered Medical Chatbot**:

   Medibot is an AI-powered medical chatbot designed to assist users by answering health-related queries. It combines the power of Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs) to provide context-aware, reliable responses. The system integrates a FAISS vector database for semantic search and is  deployed using Streamlit for a user-friendly interface.

*🚀 Features:*

✅ RAG-based Pipeline: Combines local medical knowledge with LLMs for accurate responses.

✅ FAISS Vector Store: Efficient semantic search over medical documents.

✅ Mistral LLM (Hugging Face): Generates natural, context-aware answers.

✅ Streamlit UI: An interactive web interface for chatting with Medibot.

✅ Secure API Handling: Utilizes .env files for managing sensitive keys (Hugging Face token, etc.).

*📂 Project Structure:*
.
├── vectorstore/               # Stores FAISS vector database
├── connect_memory_with_llm.py   # Python script for RAG + LLM integration
├── app.py                     # Main Streamlit application
├── requirements.txt           # Project dependencies
├── .env                       # Environment variables (API keys)
└── README.md                  # Project documentation

*⚙️ Installation:*

1.Clone the repository:

    git clone https://github.com/iamganguly-2002/Medibot.git
    cd Medibot

2.Create and activate a virtual environment:

    python -m venv .venv
    source .venv/bin/activate   # On Linux/Mac
    .venv\Scripts\activate      # On Windows

3.Install dependencies:

    pip install -r requirements.txt

4.Add your Hugging Face API key in a .env file:


    HUGGINGFACEHUB_API_TOKEN=your_token_here

5.Run the App:

    streamlit run app.py

Open the browser at http://localhost:8501 to interact with Medibot.

*🧠 Tech Stack :*

    1.Python: 3.10+

    2.Streamlit: Frontend framework for the web interface.

    3.LangChain: Framework for building the RAG pipeline.

    4.FAISS: Vector database for semantic search.

    5.Hugging Face: Utilized for the Mistral LLM.

*📌 Keywords :*

    1.Retrieval-Augmented Generation (RAG)

    2.Medical Chatbot

    3.Large Language Model (LLM)

    4.FAISS Vector Store

    5.Streamlit

*🔮 Future Scope:*

    Multilingual Support: Implement support for multiple languages to serve a wider user base.

    Speech-to-Text Integration: Allow users to interact with the chatbot using voice commands.

    Real Doctor Integration: Integrate with a database or API of certified doctors for more specific and personalized consultations.


