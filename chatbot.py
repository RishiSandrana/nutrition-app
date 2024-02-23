import streamlit as st
import vertexai
from vertexai.preview.language_models import *

project_id = "melodic-zoo-414700"
location = "us-central1"

vertexai.init(project=project_id, location=location)
chat_model = ChatModel.from_pretrained("chat-bison@002")

st.set_page_config(
    page_title="Nutrition Chatbot",
    page_icon="💬",
)

st.title("Chat with Products!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if "chat" not in st.session_state:
    st.session_state['chat'] = chat_model.start_chat(
        context = "You are designed to answer questions about food products.",
    )

if prompt := st.chat_input("Type your question"):
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

    with (st.chat_message("assistant")):
        response = st.session_state.chat.send_message(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
