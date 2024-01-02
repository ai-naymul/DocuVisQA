
import streamlit as st
import os

import google.generativeai as genai



os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="ChatBot")

st.header("ChatBot Application - Gemini Pro")

input=st.text_input("Give Your Input: ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked

if submit:

    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)