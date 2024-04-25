import streamlit as st
import pandas as pd

st.title("Dashboard")

def load_data(path:str):
    data = pd.read_csv(path)
    return data

with st.sidebar:
    upload_file = st.file_uploader("Choose a file", type=["csv", "xlsx",'pdf'])
    
    if upload_file is None:
        st.info("upload file through config",icon="ℹ️")
        st.stop()
 
        
if upload_file is not None:
    data = load_data(upload_file)
    st.dataframe(data)
