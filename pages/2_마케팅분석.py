import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st


 
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="마케팅분석",
    layout="wide"
)
 
st.title("마케팅분석")
 
df = pd.read_excel("마케팅분석.xlsx")
 
pyg_html = pyg.to_html(df)
 
components.html(pyg_html, height=1000, scrolling=True)