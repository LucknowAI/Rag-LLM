from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings


class DocSearch:
    def __init__(self, model_name, index_name, api_key):
        self.embeddings = HuggingFaceEmbeddings(model_name)
        self.docsearch = PineconeVectorStore(
            index_name=index_name,
            embedding=self.embeddings,
            pinecone_api_key=api_key,
        )


docsearch = DocSearch(
    model_name="sentence-transformers/paraphrase-MiniLM-L6-v2",
    index_name="quickstart",
    api_key="fea6d7eb-1b48-4a28-afe5-df253dbe3e1d",
)
