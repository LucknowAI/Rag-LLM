<div align="center">
<h1>Rag-LLM</h1></div>

<p align="center">
  <p align="center">Retrieval-Augmented Generation (RAG) using Large Language Models (LLMs)
</p>
</p>

 <h4 align="center">
  <a href="https://github.com/LucknowAI/Rag-LLM/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="Promptify is released under the Apache 2.0 license." />
  </a>
  <a href="http://makeapullrequest.com">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="http://makeapullrequest.com" />
  </a>
  <a href="https://discord.gg/QKw67PDZUm">
    <img src="https://img.shields.io/badge/Discord-Community-orange" alt="Community" />
  </a>
  <a href="https://github.com/LucknowAI/Lucknow-LLM/blob/main/notebooks/data_pipeline.ipynb">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="colab" />
  </a>
</h4>

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
