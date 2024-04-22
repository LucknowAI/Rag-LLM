from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings
from typing import Optional
import os
from dotenv import load_dotenv
from typing import Iterable
from pinecone import Pinecone, ServerlessSpec
from utils import create_document_list_from_local

load_dotenv()


class Create_vectordb_Pinecone:
    def create(
        DATA,
        API_KEY,
        NAME,
        DIMENSIONS,
        METRIC,
        EMBEDDING_MODEL: Optional[
            str
        ] = "sentence-transformers/paraphrase-MiniLM-L6-v2",
    ):
        pc = Pinecone(api_key=API_KEY)
        pc.create_index(
            name=NAME,
            dimension=DIMENSIONS,
            metric=METRIC,
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )
        db = PineconeVectorStore.from_documents(DATA, embedding=EMBEDDING_MODEL)
        return db


class DocSearch:
    def __init__(
        self,
        index_name,
        api_key,
        model_name: Optional[str] = "sentence-transformers/paraphrase-MiniLM-L6-v2",
    ):
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)
        self.docsearch = PineconeVectorStore(
            index_name=index_name,
            embedding=self.embeddings,
            pinecone_api_key=api_key,
        )

    def add_documents(self, path: str, chunk_size: Optional[int] = 350):
        self.docsearch.add_texts(
            texts=create_document_list_from_local(path), embedding_chunk_size=chunk_size
        )


docsearch = DocSearch(
    model_name="sentence-transformers/paraphrase-MiniLM-L6-v2",
    index_name="quickstart",
    api_key=os.getenv("PINECONE_API_KEY"),
)
