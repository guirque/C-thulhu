import sys
sys.path.append("src/")

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from controller.llm_controller import invoke, api_key_exists, update_api_key

from controller.file_controller import FileController
def initialize_session_state():
    """Initialize the session state of Streamlit"""    
    if 'uploaded_files' not in st.session_state:
        st.session_state.uploaded_files = []
    if 'file_controller' not in st.session_state:
        st.session_state.file_controller = FileController()

initialize_session_state()

st.title("🦜🔗 Quickstart App")

# Getting Gemini API Key
#if not api_key_exists():
#    value = st.sidebar.text_input("Google API Key", type="password", value=os.getenv("GEMINI_API_KEY", ""))
#    update_api_key(value)

with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not api_key_exists():
        st.warning("Please enter your Google API key!", icon="⚠")
    if submitted and api_key_exists():
        st.info(invoke(text))