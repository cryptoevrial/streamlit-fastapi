import streamlit as st
import requests

st.title("FastAPI + Streamlit Demo")

if st.button("Get Data from FastAPI"):
    response = requests.get("http://localhost:8000")
    st.write(response.json())