from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
#Here we are using Gemini-1-pro.
llm = ChatGoogleGenerativeAI(
    model="gemini-1.0-pro",
    convert_system_message_to_human=False,
    google_api_key=os.getenv("GOOGLE_API_KEY"),#re[place the GOOGLE_API_KEY with your Google API key.
    temperature=0.01,
)
