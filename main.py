#Steps for setting up virtual environment
#Set -ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# .\.venv\Scripts\activate

import streamlit as st
import os
import pandas as pd
import numpy as np
import sqlite3

db_path = db_path = 'C:/Users/parke/Github/Streamlit/database/streamlit.db'


#setting up page configuration and also adding an icon to the streamlit tab in the browser
st.set_page_config(
    page_title ="Price Increase Process",
    page_icon= "🧊",
    layout="wide"
)

#These are sections of the applicaiton that you can customize
with st.sidebar:
    st.header("Filter Pane")
    st.write("Users can use the following filters to search for specif set of contracts.")



st.title("Contract Price Increase Process")
st.header("This application is used to query existing contracts and set a new price as well as effective date.")
st.subheader("Please ensure all neccessary contracts are updated by the end of November!")



# connecting to DB


#Inatialize connection
conn = sqlite3.connect(db_path)

c = conn.cursor()

#perform query
contracts = 'select * from CONTRACTS;'
c.execute(contracts)

# fetch all results
results = c.fetchall()

# convert to dataframe
df = pd.DataFrame(results, columns=[description[0] for description in c.description])


# close connection
conn.close()

# write dataframe to application
st.subheader("List of current Contracts")
st.write(df)

