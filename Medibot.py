import streamlit as st
from connect_memory_with_llm import qa_chain  # ✅ import your RetrievalQA chain

def main():
    st.title("🩺 Medibot - Medical RAG Chatbot")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).markdown(msg["content"])

    # User input
    if prompt := st.chat_input("Ask your medical question..."):
        # Show user message
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Get response from your RAG chain
        response = qa_chain.invoke({"query": prompt})
        answer = response["result"]

        # Show assistant response
        st.chat_message("assistant").markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})

        # (Optional) Show sources
        with st.expander("📖 Sources"):
            for doc in response["source_documents"]:
                st.markdown(f"- Page {doc.metadata.get('page')}: {doc.metadata.get('source')}")


if __name__ == "__main__":
    main()
