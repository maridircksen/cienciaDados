import streamlit as st
from streamlit_extras.tags import tagger_component

tagger_component(
    content='',
    tags=[
        'Ciencia de Dados',
        'Dados Originais'
    ],
    color_name=[
        'blue',
        'lightgray'
    ]
)
colunas = st.segmented_control(
    label='Selecione as colunas',
    options=st.secrets.continuas, selection_mode='multi'
)
if len(colunas) > 0:
    tabs = st.tabs(['Dados Originais', 'Região e Estados'])
    with tabs[0]:
        st.dataframe(
            st.session_state['estados'][
                st.secrets.descritivas + colunas
            ],
            use_container_width=True,
            hide_index=True,
            height=1000
        )
    with tabs[1]:
        if st.toggle('Media'):
            regioes = st.session_state['estados'].groupby(
                st.secrets.descritivas[1]
            )[colunas].mean().reset_index()
        else:
            regioes = st.session_state['estados'].groupby(
                st.secrets.descritivas[1]
            )[colunas].sum().reset_index()
        evento = st.dataframe(
            data=regioes,
            use_container_width=True,
            hide_index=True,
            selection_mode='single-row',
            on_select='rerun'
        )
        if len(evento['selection']['rows']) > 0:
            st.dataframe(
                st.session_state['estados'][
                    st.session_state['estados']['Região'] ==
                    regioes[
                        evento['selection']['rows'][0]:
                        evento['selection']['rows'][0] + 1
                    ]['Região'].values[0]
                ][
                    st.secrets.descritivas + colunas
                ],
                use_container_width=True,
                hide_index=True
            )