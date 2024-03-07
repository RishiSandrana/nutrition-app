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
    ['Acne', 'Anxiety', 'Asthma', 'Diabetes', 'Periodontal Disease', 'Obesity'],
    key="conditions"
)

if "allergies" not in st.session_state:
    st.session_state.allergies = ""

st.session_state.allergies = st.session_state.allergies
st.text_input('Please list any food allergies you may have (e.g., milk, eggs, peanuts):', key="allergies")

if "product" not in st.session_state:
    st.session_state.product = ""

st.session_state.product = st.session_state.product
st.text_input(
    "Which product would you like to learn more about?",
    key="product",
    placeholder="20 oz Mountain Dew Baja Blast Soda Bottle",
    disabled=True
)

button = st.button("Start chat!", type="primary")
st.session_state.chat = st.session_state.chat
if button:
    llm_context = f"You are designed to answer questions about food products. The product you are being asked about is a 20 oz Mountain Dew® Baja Blast Soda Bottle. The person you're addressing is named {st.session_state.name}. {st.session_state.name} is {st.session_state.age} years old. {st.session_state.name}'s assigned gender is {st.session_state.gender}. {st.session_state.name} is affected by {st.session_state.conditions}. {st.session_state.name} is allergic to {st.session_state.allergies}."
    st.session_state.chat = chat_model.start_chat(
        context=llm_context,
        examples=[
            InputOutputTextPair(
                input_text="What are the ingredients?",
                output_text="A 20 oz Mountain Dew® Baja Blast Soda Bottle contains the following ingredients: Carbonated Water, High Fructose Corn Syrup, Natural and Artificial Flavor, Citric Acid, Sodium Benzoate (Preserves Freshness), Caffeine, Gum Arabic, Sodium Citrate, Calcium Disodium EDTA (To Protect Flavor), Sucrose Acetate Isobutyrate, Yellow 5, and Blue 1."
            ),
            InputOutputTextPair(
                input_text="Which of the product's ingredients are bad for my health?",
                output_text="Excessive amounts of High Fructose Corn Syrup (HFCS) has been linked to metabolic issues, including obesity and insulin resistance. Additionally, Yellow 5 (Tartrazine) may be linked with cancer and behavioral disorders in children, and the dye is currently banned in several European countries."
            ),
            InputOutputTextPair(
                input_text="Are there any customer reviews?",
                output_text="Yes! The 20 oz Mountain Dew® Baja Blast Soda Bottle is rated 4.3/5 stars from 57 reviews on walmart.com and 4.8/5 from 22 reviews on target.com."
            ),
            InputOutputTextPair(
                input_text="I am allergic to corn. Does this product contain any allergens?",
                output_text="Yes! The 20 oz Mountain Dew® Baja Blast Soda Bottle contains corn and its derivatives. Because of your corn allergy, I would implore you to refrain from consuming this product."
            ),
            InputOutputTextPair(
                input_text="Can you provide information about the nutritional content?",
                output_text="Certainly. A 20 oz Mountain Dew® Baja Blast Soda Bottle contains 280 calories, 0g fat, 95mg sodium, 74g total carbohydrates, including 73g added sugar, and 0g protein."
            ),
            InputOutputTextPair(
                input_text="I am male and I have acne. Is this product healthy for me?",
                output_text="No. For men, the recommended daily sugar intake is no more than 36 grams of added sugar per day. However, a 20 oz Mountain Dew® Baja Blast Soda Bottle contains 73 grams of added sugar. One study found that sugary beverages were linked to 18% higher odds of having acne: https://pubmed.ncbi.nlm.nih.gov/32520303/"
            ),
            InputOutputTextPair(
                input_text="I am male and I have anxiety. Is this product healthy for me?",
                output_text="No. For men, the recommended daily sugar intake is no more than 36 grams of added sugar per day. However, a 20 oz Mountain Dew® Baja Blast Soda Bottle contains 73 grams of added sugar. Consuming large amounts of processed sugar can trigger feelings of worry, irritability, and sadness: https://www.healthline.com/health/mental-health/surprising-foods-trigger-anxiety#added-sugar. Furthermore, this product contains 98mg of caffeine, and caffeine has been linked with anxiety and panic disorders."
            ),
            InputOutputTextPair(
                input_text="I am male and I have asthma. Is this product healthy for me?",
                output_text="No. For men, the recommended daily sugar intake is no more than 36 grams of added sugar per day. However, a 20 oz Mountain Dew® Baja Blast Soda Bottle contains 73 grams of added sugar. Sugary drinks contain large amounts of fructose corn syrup that might promote inflammation, cause chronic airway mucus hypersecretion, and eventually trigger asthmatic episodes: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8846412/#:~:text=Second%2C%20sugar%2Dsweetened%20fruit%20drinks,and%20eventually%20trigger%20asthmatic%20episodes."
            ),
            InputOutputTextPair(
                input_text="I am male and I have diabetes. Is this product healthy for me?",
                output_text="No. For men, the recommended daily sugar intake is no more than 36 grams of added sugar per day. However, a 20 oz Mountain Dew® Baja Blast Soda Bottle contains 73 grams of added sugar. You should avoid drinking sugary drinks at all costs if you have or are at risk of having diabetes. Diabetes has been linked with an increased chance of cardiovascular disease, chronic kidney disease, nonalcoholic fatty liver disease, etc."
            ),
            InputOutputTextPair(
                input_text="I am male and I have periodontal disease. Is this product healthy for me?",
                output_text="No. For men, the recommended daily sugar intake is no more than 36 grams of added sugar per day. However, a 20 oz Mountain Dew® Baja Blast Soda Bottle contains 73 grams of added sugar. High amounts of sugar intake have been linked to severe inflammation. Inflammation of the gums or in the mouth can lead to a number of severe dental problems ranging from bad breath and gum recession to tooth loss or decreased saliva production."
            ),
            InputOutputTextPair(
                input_text="I am male and I have obesity. Is this product healthy for me?",
                output_text="No. For men, the recommended daily sugar intake is no more than 36 grams of added sugar per day. Evidence suggests that diets high in added sugar promote the development of obesity."
            ),
            InputOutputTextPair(
                input_text="I am female and I have acne. Is this product healthy for me?",
                output_text="No. For women, the recommended daily sugar intake is no more than 25 grams of added sugar per day. One study found that sugary beverages were linked to 18% higher odds of having acne: https://pubmed.ncbi.nlm.nih.gov/32520303/"
            ),
            InputOutputTextPair(
                input_text="I am female and I have anxiety. Is this product healthy for me?",
                output_text="No. For women, the recommended daily sugar intake is no more than 25 grams of added sugar per day. Consuming large amounts of processed sugar can trigger feelings of worry, irritability, and sadness: https://www.healthline.com/health/mental-health/surprising-foods-trigger-anxiety#added-sugar. Furthermore, this product contains 98mg of caffeine, and caffeine has been linked with anxiety and panic disorders."
            ),
            InputOutputTextPair(
                input_text="I am female and I have asthma. Is this product healthy for me?",
                output_text="No. For women, the recommended daily sugar intake is no more than 25 grams of added sugar per day. However, a 20 oz Mountain Dew® Baja Blast Soda Bottle contains 73 grams of added sugar. Sugary drinks contain large amounts of fructose corn syrup that might promote inflammation, cause chronic airway mucus hypersecretion, and eventually trigger asthmatic episodes: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8846412/#:~:text=Second%2C%20sugar%2Dsweetened%20fruit%20drinks,and%20eventually%20trigger%20asthmatic%20episodes."
            ),
            InputOutputTextPair(
                input_text="I am female and I have diabetes. Is this product healthy for me?",
                output_text="No. For women, the recommended daily sugar intake is no more than 25 grams of added sugar per day. However, a 20 oz Mountain Dew® Baja Blast Soda Bottle contains 73 grams of added sugar. You should avoid drinking sugary drinks at all costs if you have or are at risk of having diabetes. Diabetes has been linked with an increased chance of cardiovascular disease, chronic kidney disease, nonalcoholic fatty liver disease, etc."
            ),
            InputOutputTextPair(
                input_text="I am female and I have periodontal disease. Is this product healthy for me?",
                output_text="No. For women, the recommended daily sugar intake is no more than 25 grams of added sugar per day. However, a 20 oz Mountain Dew® Baja Blast Soda Bottle contains 73 grams of added sugar. High amounts of sugar intake have been linked to severe inflammation. Inflammation of the gums or in the mouth can lead to a number of severe dental problems ranging from bad breath and gum recession to tooth loss or decreased saliva production."
            ),
            InputOutputTextPair(
                input_text="I am female and I have obesity. Is this product healthy for me?",
                output_text="No. For women, the recommended daily sugar intake is no more than 25 grams of added sugar per day. Evidence suggests that diets high in added sugar promote the development of obesity."
            )
        ]
    )
    switch_page('chatbot')