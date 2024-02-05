import streamlit as st 
import streamlit.components.v1 as stc 
import pandas as pd 
import pygwalker as pyg 

# Page Configuration
st.set_page_config(page_title="API데이터솔루션 EDA",layout="wide")

# Load Data Fxn
def load_data(data):
    return pd.read_excel(data)

def main():
    st.title("API데이터솔션으로 대시보드 만들기")

    st.subheader("스스센 통계에서 다운받은 파일을 업로드해주세요.")
    # Form
    with st.form("upload_form"):
        data_file = st.file_uploader("엑셀 파일만 업로드해주세요!") #,type=["xlsx","txt"]
        submitted = st.form_submit_button("Submit")

    if submitted:
        df = load_data(data_file)
        # Visualize
        pyg_html = pyg.walk(df,return_html=True)
        # Render with components
        stc.html(pyg_html,scrolling=True,height=1000)

    
        
    
if __name__ == "__main__":
    main()
