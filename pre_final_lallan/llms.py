"""
This file defines the settings of model used
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatGoogleGenerativeAI(
    model="gemini-1.0-pro",
    convert_system_message_to_human=False,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.01,
)
