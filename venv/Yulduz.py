import streamlit as st
from voice_assistant import uzbek_bot, russian_bot, english_bot

# Streamlit UI
st.title("Yulduz from MohirDev is online")

# Function to display user query
def display_user_query(query):
    st.write("You:")
    st.info(query)

# Function to display bot response
def display_bot_response(response):
    st.write("Voice Assistant:")
    st.success(response)

# Dropdown for selecting language
language_options = {
    "Uzbek": uzbek_bot,
    "Russian": russian_bot,
    "English": english_bot
}
selected_language = st.selectbox("Select language:", list(language_options.keys()))

# Text input for user query
query = st.text_input("You (type your query here):")

# Button to interact with the voice assistant
if st.button("Submit"):
    if query:
        display_user_query(query)
        st.write("Voice Assistant is typing...")
        language_function = language_options[selected_language]
        response = language_function(query)
        display_bot_response(response)
    else:
        st.warning("Please enter your query.")

