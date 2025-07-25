from langchain_google_genai import ChatGoogleGenerativeAI
import os

google_api_key = os.environ.get("GEMINI_API_KEY") 

model = None
try:
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=google_api_key)
except Exception:
    pass


def update_api_key(value):
    google_api_key = value
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=google_api_key)
