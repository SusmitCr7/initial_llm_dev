from dotenv import load_dotenv
load_dotenv()##load all enviroment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


##function to load Gemini Pro Model and get responses
model=genai.GenerativeModel('gemini-2.5-flash')
def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])#if input is given then give response image and input
    else:
        response=model.generate_content([image])#if no input then give the response only for image
    return response.text


#initialize the streamlit app
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini LLM Application")
input=st.text_input("Input Prompt: ",key="input")

uploaded_file=st.file_uploader("Choose an image ...",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image.",use_container_width=True)
        
submit=st.button("Tell me about the image")


##if submit is clicked
if submit:
    
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)
