from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## function to load Gemini Pro model and get repsonses
model = genai.GenerativeModel('gemini-2.5-pro')
chat=model.start_chat(history=[])


def get_gemini_response(question):
    response=chat.send_message(question,stream=True)#stream is enabled so that we donot have to wait for the LLM to give the whole response
    response
    


##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")



# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]
  
    
input=st.text_input("Input",key="input")
submit=st.button("Ask the question")


if submit and input:
    response=get_gemini_response(input)
    ##Add user query and response to session chat history
    st.session_state['chat_history'].append(("You",input))#we are appending the inputs into the You variable
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))
        #as soon as we are getting the response we are displaying and accordingly we are also appening in chat_history
    

st.subheader("The Chat history is")

for role,text in st.session_state['chat_history']:#3wbatever histriy is there it is in the key value pair of you and bot
    st.write(f"{role}: {text}")