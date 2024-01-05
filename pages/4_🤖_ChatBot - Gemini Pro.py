
import streamlit as st
import os

import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import os

# Fetch the API key from the environment variable
api_key = os.getenv("GOOGLE_API_KEY")




# Use the API key
genai.configure(api_key=api_key)
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="ChatBot")


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







st.header("ChatBot Application - Gemini Pro")

input=st.text_input("Give Your Input: ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked

if submit:

    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)