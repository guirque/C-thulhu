FROM python:alpine

# Dependencies include LangChain, Streamlit, Flask
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["streamlit", "run", "src/view/index.py"]