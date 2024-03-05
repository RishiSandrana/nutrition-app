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
    st.session_state.name = ""

st.session_state.name = st.session_state.name
st.text_input("What's your name?", key="name")

if "age" not in st.session_state:
    st.session_state.age = 1

st.session_state.age = st.session_state.age
st.slider('How old are you?', 1, 100, key="age")

if "gender" not in st.session_state:
    st.session_state.gender = "Male"

st.session_state.gender = st.session_state.gender
st.radio(
    "What was your assigned gender at birth?",
    ["Male", "Female", "Prefer not to disclose"],
    index=0,
    horizontal=True,
    key="gender"
)

if "conditions" not in st.session_state:
    st.session_state.conditions = []

st.session_state.conditions = st.session_state.conditions
st.multiselect(
    'Are any of the following medical conditions applicable to you?',
    ['Acne', 'Anxiety', 'Asthma', 'Cardiovascular Disease', 'Chronic Kidney Disease', 'Diabetes', 'Inflammation', 'Non-Alcoholic Fatty Liver Disease', 'Peridontal Disease', 'Obesity'],
    key="conditions"
)

if "allergies" not in st.session_state:
    st.session_state.allergies = ""

st.session_state.allergies = st.session_state.allergies
st.text_input('Please list any food allergies you may have (e.g., milk, eggs, peanuts):', key="allergies")

button = st.button("Start chat!", type="primary")
if button:
    llm_context = f"You are designed to answer questions about food products. The person you're addressing is named {st.session_state.name}. They are {st.session_state.age} years old. Their assigned gender is {st.session_state.gender}. They are affected by {st.session_state.conditions}. They are allergic to {st.session_state.allergies}."
    st.session_state.chat = chat_model.start_chat(context=llm_context)
    switch_page('chatbot')