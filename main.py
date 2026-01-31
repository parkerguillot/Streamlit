#Steps for setting up virtual environment
#Set -ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#.\.venv\Scripts\activate

import streamlit as st

st.set_page_config(
    page_title ="Multipage App",
    page_icon= "🧊",
)

st.title("This is a title!")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")

st.header("This is the Header section of the main page.")

st.sidebar.success("Select a page above.")
