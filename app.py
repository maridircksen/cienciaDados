import pandas as pd
import streamlit as st
import json

@st.cache_data
def load_database():
    st.session_state['estados'] = pd.read_parquet(st.secrets.dados)
    st.session_state['geo'] = json.load(open(st.secrets.mapa))

st.set_page_config(
    layout='wide',
    page_title='Ciencia de Dados',
    initial_sidebar_state='expanded'
)

load_database()

pages = {
    'CIENCIA DE DADOS': [],
    'Tabela de dados': [
        st.Page(
            page='tabela/dadosoriginais.py',
            title='Dados Originais',
            icon=':material/table:'
        )
    ],
    'Estatística Univariada': [
        st.Page(
            page='estatistica/univariada/curvaabc.py',
            title='Curva ABC',
            icon=':material/leaderboard:'
        )
    ]
}
pg = st.navigation(pages, expanded=True)
pg.run()