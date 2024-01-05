import streamlit as st

# Set the page config
st.set_page_config(page_title="DocsVisqa", page_icon='✨')

# Add a header
st.header("DocsVisqa")
st.markdown("""
This project is a multi-functional application that leverages the power of Google's Gemini Pro API to provide various services such as searching within PDFs, image recognition, and chatbot functionality. 🚀

## Features 🛠️

1. **PDF Search** 📄: This feature allows users to upload a PDF file and ask questions related to the content of the PDF. The application will then search within the PDF and provide the most relevant answer. This can be particularly useful for quickly finding information within large documents.

2. **Image Recognition** 🖼️: This feature allows users to upload an image and ask questions about it. The application will then analyze the image and provide a response. This can be useful for understanding the content of an image without manual inspection.

3. **Chatbot** 🤖: This feature allows users to interact with a chatbot powered by the Gemini Pro API. The chatbot can answer a wide range of questions and provide useful information.

## Impact 💡

This application can significantly improve productivity by automating the process of searching for information within documents and images. It can also provide quick and accurate responses to various questions, reducing the need for manual research.

## How to Use 📖

To use this application, simply navigate to the desired feature (PDF Search, Image Recognition, or Chatbot) and follow the prompts. For PDF Search and Image Recognition, you will need to upload a file. For the Chatbot, simply type your question into the input field and press "Ask the question". 🖱️
""")


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

