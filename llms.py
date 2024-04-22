from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.0-pro",
    convert_system_message_to_human=False,
    google_api_key="AIzaSyCMAvB0-ehycivbI10OaaqY9WNXUe20U7U",
    temperature=0.01,
)
