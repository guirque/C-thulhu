import sys
sys.path.append("src/")

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from controller.llm_controller import invoke, api_key_exists, update_api_key
import os
import easygui
from streamlit.logger import get_logger

MAX_MESSAGES = 15

LOGGER = get_logger(__name__)
st.set_page_config(page_title="Folder Organizer AI", page_icon="📄")

st.title("📄💾 Folder Organizer AI")

value = st.sidebar.text_input("Google API Key", type="password", value=os.getenv("GEMINI_API_KEY", ""))
if value != os.getenv("GEMINI_API_KEY", ""):
    update_api_key(value)

def initialize_session_state():
    """Initialize the session state of Streamlit"""    
    if "folder_path" not in st.session_state:
        st.session_state.folder_path = None
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "How can I help you to organize your folders?"}]

initialize_session_state()

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not api_key_exists():
        st.info("Please add your Google Gemini key to continue.")
        st.stop()

    LOGGER.info(f"user prompt: {prompt}")

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    if not st.session_state.folder_path:
        st.error("Folder not selected")
    else:
        response = invoke(st.session_state.messages, st.session_state['folder_path'])
        msg = response['messages'][-1].content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)

    if len(st.session_state.messages) > MAX_MESSAGES:
        st.session_state.messages = st.session_state.messages[-MAX_MESSAGES:]

with st.container():
    st.markdown("### Working Directory")
    if st.button("📁 Choose Folder"):
        folder = easygui.diropenbox("Select a folder")
        if folder:
            st.session_state.folder_path = folder
            st.session_state.messages.append({"role": "system", "content": f"Selected folder: {folder}"})
            st.chat_message("system").write(f"Selected folder: {folder}")
            LOGGER.info(f"set selected folder to {folder}")