import streamlit as st
import vertexai
from vertexai.preview.language_models import *
from streamlit_extras.switch_page_button import switch_page

project_id = "melodic-zoo-414700"
location = "us-central1"

vertexai.init(project=project_id, location=location)
chat_model = ChatModel.from_pretrained("chat-bison@002")

st.set_page_config(
    page_title= "Nutrition Chatbot",
    page_icon= "⚙️",
)

st.title("User Preferences")

if "chat" not in st.session_state:
    st.session_state.chat = chat_model.start_chat()

if "name" not in st.session_state:
    st.session_state.name = st.text_input("What's your name?")
else:
    st.session_state.name = st.text_input("What's your name?", value=st.session_state.name)

if "age" not in st.session_state:
    st.session_state.age = st.slider('How old are you?', 1, 100)
else:
    st.session_state.age = st.slider('How old are you?', 1, 100, st.session_state.age)

if "allergies" not in st.session_state:
    st.session_state.allergies = st.multiselect('Are you allergic to any of the following?',
                                                ['Milk', 'Eggs', 'Fish', 'Crustacean shellfish', 'Tree nuts', 'Peanuts',
                                                 'Wheat', 'Soybeans', 'Sesame'])
else:
    st.session_state.allergies = st.multiselect('Are you allergic to any of the following?',
                                                ['Milk', 'Eggs', 'Fish', 'Crustacean shellfish', 'Tree nuts', 'Peanuts',
                                                 'Wheat', 'Soybeans', 'Sesame'], default=st.session_state.allergies)

button = st.button("Start chat!", type="primary")
if button:
    llm_context = f"You are designed to answer questions about food products. The person you're addressing is named {st.session_state.name}. They are {st.session_state.age} years old. They are allergic to {st.session_state.allergies}."
    st.session_state.chat = chat_model.start_chat(context=llm_context)
    switch_page('chatbot')