import sys
sys.path.append("src/")

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from controller.llm_controller import invoke, api_key_exists, update_api_key
import os
import easygui

st.title("🦜🔗 Folder organizer AI")

value = st.sidebar.text_input("Google API Key", type="password", value=os.getenv("GEMINI_API_KEY", ""))
update_api_key(value)


with st.form("working_dir"):
    submitted = st.form_submit_button("Choose AI Working Directory")
    if submitted:
        st.session_state['folder_path'] = easygui.diropenbox("Select a folder")

with st.form("submit"):
    text = st.text_area(
        "Type the criteria that you want for reorganizing your files:",
        "Documents that look have similar subjects",
    )

    submitted = st.form_submit_button("Run")
    if not api_key_exists():
        st.warning("Please enter your Google API key!", icon="⚠")
    if submitted and api_key_exists():
        if not st.session_state['folder_path']:
            st.error("Folder not selected")
        else:
            st.info(invoke(text, st.session_state['folder_path']))