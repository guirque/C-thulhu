from langchain_google_genai import ChatGoogleGenerativeAI
import os
from langgraph.prebuilt import create_react_agent
from model.tools.toolkit import tookit
from dotenv import load_dotenv
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

load_dotenv()
google_api_key = os.environ.get("GEMINI_API_KEY") 

model = None

# Model Creation ----------------------------------------------------------------------------------

def create_model(google_api_key):
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=google_api_key)
    model = create_react_agent(llm, tookit, prompt="You are a file management assistant. Your job is to help the user organize their files, create new files and know about the files in a specified folder. You can use the tools provided. Multiple, if needed.")
    LOGGER.info(f"LLM model created")
    return model

try:
    model = create_model(google_api_key)
except:
    LOGGER.fatal(f"failed to create model")


def update_api_key(value):
    google_api_key = value
    model = create_model(google_api_key)

# LLM Calling -------------------------------------------------------------------------------------

def invoke_llm(messages):
    return model.invoke({"messages": messages})