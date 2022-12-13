import streamlit as st
import pandas as pd 
import plotly.express as px
import numpy as np


# Customizar a aba da janela do APP
st.set_page_config(page_icon=r'\projetos\ProjetoFinal\streamlit\barchart.png',page_title='2compare')

#---------- Cabeçalho do App------------------
a,b = st.columns([2,14])

with a:
    st.image(r'\projetos\ProjetoFinal\streamlit\barchart.png')
with b:
    st.title('2compare - Analisando cursos')
#---------- Cabeçalho do App------------------

with st.expander('_Do que se trata esse app?_', True):
    st.markdown('''
        Este aplicativo visa comparar a evasão entre os turnos diurno (matutino e vespertino) e norturno dos cursos oferecidos pelo 
        Centro de Ciências Sociais Aplicadas da Universidade Federal da Paraíba.
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

#----------média evasão----------
media = df_selection['evasão'].mean()

df_dia = df_selection.loc[df_selection['turno']=='diurno']
media_dia = df_dia['evasão'].mean()

df_noite = df_selection.loc[df_selection['turno']=='noturno']
media_noite = df_noite['evasão'].mean()

diferenca = np.round(media_noite - media_dia)
#----------média evasão----------

estudantes = df_selection['ingressantes'].sum()
#leftovers = estudantes*(media/100)
def leftovers():
    if media_noite > media_dia:
        return int((((media_noite-media_dia)*estudantes)/100)/5)
    elif media_dia > media_noite:
        return int(((media_dia-media_noite)*estudantes)/100)
    else:
        return np.nan

col1, col2, col3 = st.columns(3)
#---------plotagem-------------
with col1:
    st.metric(
        label='Evasão Média (%): ',
        value=np.round(media)
    )

with col2:
    st.metric(
        label='Diferença entre turnos (%): ',
        value=diferenca
    )

with col3:
    st.metric(
        label='Diferença de desistentes (ano): ',
        value=np.round(leftovers())
    )


fig_evasao = px.bar(df_selection,
    x='evasão',
    y='ano',
    color='turno',
    barmode='group'
)

st.plotly_chart(fig_evasao)
#---------plotagem-------------
