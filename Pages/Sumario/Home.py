import datetime as dt
import streamlit as st
import pandas as pd
import seaborn as sns
sns.set(font_scale=3)


def page_home():
    hoje = dt.datetime.now()
    hoje = dt.datetime.strftime(hoje, '%d/%m/%Y')
    st.title(f'Análise Sentimento da Economia Brasileira {hoje}')
    st.image('grafico.png')

    import matplotlib.pyplot as plt
    st.write('Análise Geral:')
    df = pd.read_csv('df_analytcs_sentiment_final.csv')
    fig = plt.figure(figsize=(20, 10))
    sns.countplot(data = df, y= 'Sentimento', palette = ['white', 'green','red'], saturation=0.90)
    st.pyplot(fig)

    import matplotlib.pyplot as plt
    st.write('Análise por Horário:')
    df = pd.read_csv('df_analytcs_sentiment_final.csv')
    fig = plt.figure(figsize=(20, 10))
    sns.lineplot(data = df, y = 'Sentimento', x = 'Hora')
    st.pyplot(fig)