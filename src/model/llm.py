from langchain_google_genai import ChatGoogleGenerativeAI
import os
from langgraph.prebuilt import create_react_agent
from model.tools.toolkit import tookit
from langchain_core.messages import HumanMessage

google_api_key = os.environ.get("GEMINI_API_KEY") 

model = None

# Model Creation ----------------------------------------------------------------------------------

def create_model(google_api_key):
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=google_api_key)
    model = create_react_agent(llm, tookit)
    return model

try:
    model = create_model(google_api_key)
except:
    print("Failed to create model. ")

def update_api_key(value):
    google_api_key = value
    model = create_model(google_api_key)

# LLM Calling -------------------------------------------------------------------------------------

def invoke_llm(prompt):
    return model.invoke({"messages": HumanMessage(prompt)})