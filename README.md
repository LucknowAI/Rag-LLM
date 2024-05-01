# Rag-LLM

Retrieval-Augmented Generation (RAG) using Large Language Models (LLMs)

<img width="1499" alt="Screenshot 2024-05-01 at 7 27 33 PM" src="https://github.com/LucknowAI/Rag-LLM/assets/17107749/885b84e5-c0e2-4b4b-bfbd-6451395093e9">


## Usage

1. **Streamlit UI Interface**
   The Streamlit UI interface provides an interactive way to check the Lallan RAG LLM. To use it, run the following command in your terminal:

   ```bash
   streamlit run ui.py
   ```

   This command starts the Streamlit server and opens the application in your web browser.

2. **API for RAG Chain**
   An API for the RAG Chain has been created to allow other applications to use the RAG LLM. The base URL for the API will be provided shortly after hosting. This will allow you to make HTTP requests to the API and receive responses from the RAG LLM.

3. **API for local RAG Chain**
   ```bash
   uvicorn fp:app --reload
   ```
Stay tuned for more updates and features!
