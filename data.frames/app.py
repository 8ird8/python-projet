import pandas as pd  
import plotly_express as px  
import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation



st.set_page_config(page_title='Covid-19 statistics ',
                   page_icon="🌍"
                   )



with st.container():
    st.title("Covid-19 Dashboard")

    ###################################
    

    st.header("  Statistiques Confirmed Cases " )

    

    data = {'Countries': ['USA', 'India', 'France' , 'Germany' , 'Brazil'],
            'Total Cases': [104196861,44682784,39524311,37779833,36824580]}
    df = pd.DataFrame(data)

    
    ######### BAR CHART 
    

    fig = px.bar(df, x='Countries', y='Total Cases', color='Countries',
                 labels={'Countries': 'Countries', 'Total Cases': 'Total Cases'})

    #------Bar Chart Modifications-------:
    

    
    st.plotly_chart(fig)

    ##############################

    

    st.title(" Total Recovered Cases ")

    #Building Data :



    Countries_ASIA = ['India', 'Japan', 'Korea']
    Countries_EUR = ['Italy', 'Uk', 'France']
    Recovered_Cases_ASIA = [44150289, 215670425, 29740877]
    Recovered_Cases_EUR = [25014986, 24020088, 39264546]

    df_RC_ASIA = pd.DataFrame({'Countries': Countries_ASIA, 'Total Recovered Cases': Recovered_Cases_ASIA})
    df_RC_EUR = pd.DataFrame({'Countries': Countries_EUR, 'Total Recovered Cases': Recovered_Cases_EUR})

    figure, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].plot(df_RC_ASIA['Countries'], df_RC_ASIA['Total Recovered Cases'], c='m')
    axes[0].set_title(' Recovered Cases in some countries among ASIA')

    

    axes[1].plot(df_RC_EUR['Countries'], df_RC_EUR['Total Recovered Cases'], c='r')
    axes[1].set_title(' Recovered Cases in some countries among EUROPE')

    st.pyplot(figure)

    st.title("  Total Deaths  ")

    #DataFrame

    labels = ['Japan', 'Korea' , 'Italy' , 'UK' , 'Russia']
    Deaths = [68399, 33486 , 186833 , 204171 , 395108]
    explode = [0, 0, 0, 0, 0.1]

    # Create & Customize a pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(Deaths, labels=labels, autopct='%1.1f%%', startangle=90 ,wedgeprops={'edgecolor':'black'} ,explode=explode,
            shadow=False)
    ax1.axis('equal')

    # Display the chart in Streamlit
    st.pyplot(fig1)

