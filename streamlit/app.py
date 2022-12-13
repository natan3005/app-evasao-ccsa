import streamlit as st
import pandas as pd 
import plotly.express as px
import numpy as np


# Customizar a aba da janela do APP
st.set_page_config(page_icon='📊', page_title='2compare')

#---------- Cabeçalho do App------------------
a,b = st.columns([1,10])

with a:
    st.image('\projetos\ProjetoFinal\streamlit\logo.png')
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

#df_dia = df_selection[['evasão','turno']]
#dk = df_selection.loc[df_selection['turno']=='diurno']

df_dia = df_selection.loc[df_selection['turno']=='diurno']
media_dia = df_dia['evasão'].mean()

df_noite = df_selection.loc[df_selection['turno']=='noturno']
media_noite = df_noite['evasão'].mean()

diferenca = np.round(media_noite - media_dia)

col1, col2, col3 = st.columns(3)
#---------plotagem-------------
with col1:
    st.metric(
        label='Evasão Média: ',
        value=np.round(df_selection['evasão'].mean())
    )

with col2:
    st.metric(
        label='Diferença Evasão: ',
        value=diferenca
    )

##with col3:
    #st.metric(
    #    label='Não concluiram a graduação: ',
    #    value=np.round(df_selection['evasão'].sum())
    #)


fig_evasao = px.bar(df_selection,
    x='evasão',
    y='ano',
    color='turno',
    barmode='group'
)

st.plotly_chart(fig_evasao)
#---------plotagem-------------
