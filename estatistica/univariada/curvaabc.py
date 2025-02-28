import pandas as pd 
import streamlit as st

def classificacao_abc_variavel(abc, variavel):
    abc['percentual'] = abc[variavel] / abc[variavel].sum()
    abc_sort = abc.sort_values(by=variavel, ascending=False)
    abc_sort['percentual_acumulado'] = abc_sort['percentual'].cumsum()
    abc_sort['classe'] = abc_sort['percentual_acumulado'].apply(
        lambda x: 'A' if x <= 0.65 else ('B' if x <= 0.90 else 'C')
    )
    return abc_sort 

variavel = st.segmented_control(
    'Selecione a variavel', options=st.secrets.continuas, selection_mode='single'
)
if variavel is not None:
    estados_abc = classificacao_abc_variavel(
        st.session_state['estados'][st.secrets.descritivas + [variavel]].copy(), variavel
    )
    st.dataframe(estados_abc)
