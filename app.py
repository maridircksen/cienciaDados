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
        ),
        st.Page(
            page='estatistica/univariada/classes.py',
            title='Classes',
            icon=':material/equalizer:'
        ),
        st.Page(
            page='estatistica/univariada/anova.py',
            title='Análise de Variância (ANOVA)',
            icon=':material/candlestick_chart:'
        )
    ],
    'Estatística Multivariada': [
        st.Page(
            page='estatistica/multivariada/correlacao.py',
            title='Correlação',
            icon=':material/pivot_table_chart:'
        ),
        st.Page(
            page='estatistica/multivariada/regressaolinear.py',
            title='Regressão Linear',
            icon=':material/show_chart:'
        ),
        st.Page(
            page='estatistica/multivariada/vif.py',
            title='Fator de Variação de Inflação',
            icon=':material/leaderboard:'
        ),
    ]
}
pg = st.navigation(pages, expanded=True)
pg.run()