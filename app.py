import streamlit as st

from chatbot.faq_engine import FAQChatbot


st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

faq_path = os.path.join(
    BASE_DIR,
    "data",
    "faq.csv"
)

bot = FAQChatbot(faq_path)

st.title("🤖 AI FAQ Chatbot")
st.markdown(
    "### CodeAlpha Internship Project"
)

st.write("---")

question = st.text_input(
    "Ask a Question"
)

if st.button("Send"):

    if question.strip():

        response = bot.get_response(
            question
        )

        st.success("Response")

        st.write(response)

    else:
        st.warning(
            "Please enter a question."
        )