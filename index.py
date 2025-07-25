import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Carrega as variáveis do .env
load_dotenv()

st.title("🦜🔗 Quickstart App")

google_api_key = st.sidebar.text_input("Google API Key", type="password", value=os.getenv("GOOGLE_API_KEY", ""))


def generate_response(input_text):
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=google_api_key)
    st.info(model.invoke(input_text))


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not google_api_key:
        st.warning("Please enter your Google API key!", icon="⚠")
    if submitted and google_api_key:
        generate_response(text)