import streamlit as st
import os
import pandas as pd
import numpy as np

st.title("Projects")


st.markdown("This is created using st.markdown.")

# this is a way to add user input into your application
x = st.slider("Choose an x value",1,10)

# THis is how stremalit will dispaly values or write them in the application without specifying print in terminal
st.subheader("st.write")
st.write("The value of :red[***x***] is ",x)

# with st.columns, you can specifiy different number of columns for your streamlit application
st.subheader("st.column")
col1, col2 = st.columns(2)
with col1:
    y = st.slider("Choose an y value",1,10)

with col2:
    st.write("The value of :blue[***y***] is ",y)

st.subheader("st.area_chart")
chart_data = pd.DataFrame(np.random.randn(20,3),columns=["a","b","c"])
st.area_chart(chart_data)