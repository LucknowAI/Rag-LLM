# Rag-LLM

Retrieval-Augmented Generation (RAG) using Large Language Models (LLMs)

## Usage

1. **Streamlit UI Interface**
   The Streamlit UI interface provides an interactive way to check the Lallan RAG LLM. To use it, run the following command in your terminal:

   ```bash
   streamlit run ui.py
   ```

   This command starts the Streamlit server and opens the application in your web browser.

2. **API for RAG Chain**
   An API for the RAG Chain has been created to allow other applications to use the RAG LLM. The base URL for the API will be provided shortly after hosting. This will allow you to make HTTP requests to the API and receive responses from the RAG LLM.

Stay tuned for more updates and features!
3. **API for local RAG Chain**
   ```bash
   uvicorn fp:app --reload
   ```

