import streamlit as st
import pandas as pd
import seaborn as sns
import mplcyberpunk
import matplotlib.pyplot as plt
plt.style.use('cyberpunk')
import datetime as dt
import Pages.Sumario.Home as homepage
import Pages.Sumario.Tweets as tweetpage
st.sidebar.title('Menu')
page = st.sidebar.selectbox('Selecionar',['Graficos','Tweets'])

if page == 'Graficos':
    homepage.page_home()
    plt.clf()

if page == 'Tweets':
    tweetpage.page_tweet()

