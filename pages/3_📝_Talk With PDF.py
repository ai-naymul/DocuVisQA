import streamlit as st

import google.generativeai as genai
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma

from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

import io
import tempfile

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.



import os

# Fetch the API key from the environment variable
api_key = os.getenv("GOOGLE_API_KEY")

# Use the API key
genai.configure(api_key=api_key)



def load_pdf_split(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.read()

        # Convert bytes data to a BytesIO object
        file_like_object = io.BytesIO(bytes_data)

        # Save BytesIO object to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file_like_object.read())
            tmp_path = tmp.name

        # Use the temporary file path to load the PDF
        loader = PyPDFLoader(tmp_path)
        pages = loader.load_and_split()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        content = "\n\n".join(str(page.page_content) for page in pages)

        texts = text_splitter.split_text(content)
        print(len(texts))
        print(texts[0])
        return texts
    else:
        # Handle the case when uploaded_file is None
        raise ValueError("No file was uploaded.")

    


def load_model():
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001", google_api_key=api_key)

    chat_model_pdf =  ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.4, google_api_key=api_key, convert_system_message_to_human=True)
    return chat_model_pdf, embeddings

def store_vector(texts, embeddings):
      vector_database = Chroma.from_texts(texts, embeddings).as_retriever()
      return vector_database

def question_chain_response(chat_model_pdf,vector_database, user_input):
    chain = load_qa_chain(chat_model_pdf, chain_type='stuff')
    docs = vector_database.get_relevant_documents(user_input)

    response = chain({'input_documents': docs, 'question': user_input}, return_only_outputs=True)

    print(response)
    return response


st.set_page_config(page_title="DocUVisQA - Talk With Your Image and PDF")




# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# Load Animation
animation_symbol = "❄"

st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True,
)



st.header("Talk With You PDF - Gemini Pro")
user_input = st.text_input("Give Your Prompt Here: ",key="input")
uploaded_file = st.file_uploader("Choose Your Pdf File", type='pdf')
pdf = ''
submit=st.button("Tell me about the PDF")
if uploaded_file and submit:
     texts = load_pdf_split(uploaded_file)
     chat_model_pdf, embeddings = load_model()
     vector_database = store_vector(texts, embeddings)
     response = question_chain_response(chat_model_pdf,vector_database, user_input)
     st.subheader("The Response is")
     st.write(response['output_text'])
