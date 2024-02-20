import streamlit as st
import vertexai
from vertexai.preview.generative_models import GenerativeModel

project_id = "melodic-zoo-414700"
location = "us-central1"

vertexai.init(project = project_id, location=location)
model = GenerativeModel('gemini-pro')

st.set_page_config(
    page_title= "Nutrition Chatbot",
    page_icon= "💬",
)

st.title("Chat with Products!")

if prompt := st.chat_input("Type your question"):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        chat = model.start_chat(response_validation=False)
        output = chat.send_message(prompt).text
        response = st.write(output)