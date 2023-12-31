import streamlit as st
from PIL import Image

import google.generativeai as genai
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma

from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI



GOOGLE_API_KEY='AIzaSyD3ppjOkpyQCxuZmEFKy-V3mTAhaAnypnw'
genai.configure(api_key=GOOGLE_API_KEY)






loader = PyPDFLoader("lol.pdf")
pages = loader.load_and_split()
# print(pages)



text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
content = "\n\n".join(str(page.page_content) for page in pages)


texts = text_splitter.split_text(content)

print(len(texts))
print(texts[0])

embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001", google_api_key=GOOGLE_API_KEY)

vector_database = Chroma.from_texts(texts, embeddings).as_retriever()

chat_model_pdf = model = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.4, google_api_key=GOOGLE_API_KEY, convert_system_message_to_human=True)

chain = load_qa_chain(chat_model_pdf, chain_type='stuff')

question = input('Enter your question')
docs = vector_database.get_relevant_documents(question)

response = chain({'input_documents': docs, 'question': question}, return_only_outputs=True)

print(response)





# def get_gemini_response(input,image,prompt):
#     model = genai.GenerativeModel('gemini-pro-vision')
#     response = model.generate_content([input,image[0],prompt])
#     return response.text
    

# def input_image_setup(uploaded_file):
#     # Check if a file has been uploaded
#     if uploaded_file is not None:
#         # Read the file into bytes
#         bytes_data = uploaded_file.getvalue()

#         image_parts = [
#             {
#                 "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
#                 "data": bytes_data
#             }
#         ]
#         return image_parts
#     else:
#         raise FileNotFoundError("No file uploaded")


# ##initialize our streamlit app

# st.set_page_config(page_title="Gemini Image Demo")

# st.header("Gemini Application")
# input=st.text_input("Input Prompt: ",key="input")
# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
# image=""   
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image.", use_column_width=True)


# submit=st.button("Tell me about the image")

# input_prompt = """
#                You are an expert in understanding invoices.
#                You will receive input images as invoices &
#                you will have to answer questions based on the input image
#                """

# ## If ask button is clicked

# if submit:
#     image_data = input_image_setup(uploaded_file)
#     response=get_gemini_response(input_prompt,image_data,input)
#     st.subheader("The Response is")
#     st.write(response)