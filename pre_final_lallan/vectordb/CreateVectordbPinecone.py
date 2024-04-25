from dotenv import load_dotenv
from typing import Optional
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

load_dotenv()


class CreateVectordbPinecone:
    """
    This class provides methods to create vector databases using pinecone
    """
    @staticmethod
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
