import streamlit as st
import vertexai
from vertexai.preview.generative_models import GenerativeModel

project_id = "melodic-zoo-414700"
location = "us-central1"

vertexai.init(project=project_id, location=location)
model = GenerativeModel('gemini-pro')

st.set_page_config(
    page_title="Nutrition Chatbot",
    page_icon="💬",
)

st.title("Chat with Products!")

if "messages" not in st.session_state:
    st.session_state.messages = []

if prompt := st.chat_input("Type your question"):
    with st.chat_message("user"):
        st.session_state.messages.append(prompt)
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = model.generate_content(st.session_state.messages)
        st.markdown(response.text)
