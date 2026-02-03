import streamlit as st
import requests

API_URL = "https://contract-risk-api.onrender.com/api/ai/contract-risk"
# ↑ replace with your actual Node Render URL if different

st.set_page_config(page_title="Contract Risk Bot")
st.title("📄 Contract Risk Analysis Bot")

text = st.text_area(
    "Paste contract text here",
    height=220,
    placeholder="Enter contract clauses here..."
)

if st.button("Analyze Risk"):
    if not text.strip():
        st.warning("Please enter contract text")
    else:
        with st.spinner("Analyzing contract..."):
            response = requests.post(
                API_URL,
                json={"contractText": text},
                timeout=30
            )
            st.subheader("Risk Analysis Result")
            st.json(response.json())
