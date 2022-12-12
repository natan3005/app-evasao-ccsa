import streamlit as st
import pandas as pd 
import plotly.express as px
import numpy as np


# Customizar a aba da janela do APP
st.set_page_config(page_icon='📊', page_title='2compare')

#---------- Cabeçalho do App------------------
a,b = st.columns([1,10])

with a:
    st.image('\projetos\ProjetoFinal\streamlit\logo.png.png')
with b:
    st.title('Comparando a Evasão no CCSA')
#---------- Cabeçalho do App------------------


st.markdown('''
     Este App visa comparar a evasão dos cursos oferecidos pelo 
     Centro de Ciências Sociais Aplicadas na Universidade Federal da Paraíba.
''')


#---------sidebar-------------
df = pd.read_excel(r'\projetos\ProjetoFinal\tables\ccsa.xlsx',
    parse_dates=[2]
)

st.sidebar.header('Filtre aqui 🔍')

curso = st.sidebar.multiselect(
    'Selecione o curso: ',
    options= df['NO_CINE_ROTULO'].unique(),
    default= df['NO_CINE_ROTULO'].unique()
)

turno = st.sidebar.multiselect(
    'Selecione o turno: ',
    options=df['turno'].unique(),
    default= df['turno'].unique()
)
#---------sidebar-------------

df_selection = df.query(
    'NO_CINE_ROTULO == @curso & turno == @turno'
)

#---------plotagem-------------

fig_evasao = px.bar(df_selection,
    x='evasão',
    y='ano'
)

st.plotly_chart(fig_evasao)

#---------plotagem-------------

#st.dataframe(df_selection)

#curso = st.selectbox('Selecione o curso que deseja analisar:',options=['Administração','Arquivologia','Biblioteconomia','Ciências atuariais','Contabilidade','Economia','Gestão pública','Relações internacionais',''])
#if curso:
#    df = pd.read_excel(r'\projetos\ProjetoFinal\ccsa.xlsx')
#    df = df.loc[df['NO_CINE_ROTULO']==curso]
#    st.dataframe(df)