from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings
from typing import Optional


class DocSearch:
    def __init__(self, index_name, api_key, model_name: Optional[str] = 'sentence-transformers/paraphrase-MiniLM-L6-v2'):
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)
        self.docsearch = PineconeVectorStore(
            index_name=index_name,
            embedding=self.embeddings,
            pinecone_api_key=api_key,
        )



docsearch = DocSearch(
    model_name="sentence-transformers/paraphrase-MiniLM-L6-v2",
    index_name="quickstart",
    api_key=os.getenv("PINECONE_API_KEY"),
)
