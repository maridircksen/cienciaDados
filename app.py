import pandas as pd 
import streamlit as st
import json

@st.cache_data
def load_database():
    st.session_state['estados'] = pd.read_parquet(st.secrets.dados)
    st.session_state['geo'] = json.load(open(st.secrets.mapa))

st.set_page_config(
    layout="wide",
    page_title="Ciência de Dados",
    initial_sidebar_state="expanded"
)

load_database()
st.write('Deve funcionar!')