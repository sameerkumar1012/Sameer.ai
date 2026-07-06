import streamlit as st
import requests

API_URL = "http://backend:8000"

st.set_page_config(
    page_title="PortfolioGPT",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Sameer.AI")
st.write("Ask anything about Sameer.")

question = st.text_input(
    "Ask a question",
    placeholder="Example: Tell me about Sameer's projects"
)

if st.button("Ask"):

    if question.strip():

        with st.spinner("Thinking..."):

            response = requests.get(
                f"{API_URL}/faq/search",
                params={"question": question}
            )

            if response.status_code == 200:
                data = response.json()
                st.markdown(data["markdown"])
            else:
                st.error("Something went wrong. Please try again.")