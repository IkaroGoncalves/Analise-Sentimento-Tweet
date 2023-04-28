import streamlit as st
import pandas as pd

def page_tweet():
    st.title('Tweets do dia')
    df = pd.read_csv('df_analytcs_sentiment_final.csv')
    df = df.loc[0:499, ['Data', 'ID', 'Tweets','Sentimento']]
    st.dataframe(df)

