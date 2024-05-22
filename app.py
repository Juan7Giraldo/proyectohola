import pandas as pd
import streamlit as st
import plotly_express as px

st.title('Análisis Exploratorio de Datos de Anuncios de Ventas de Coches')


car_data = pd.read_csv('archivo_proyecto.csv')
hist_button = st.button('construir histograma')

if hist_button:
    st.write('creacion de un histograma para el conjunto de datos de anuncios de ventas de coches')
    fig = px.histogram(car_data, x ='odometer')
    st.plotly_chart(fig,use_container_width= True)
    
grafico_button = st.button('construir grafico de dispersion')    
if grafico_button:
    st.write('creacion de un grafico de dispersion para el conjunto de datos de anuncios de ventas de coches')
    fig = px.scatter(car_data, x ='odometer',y = 'price')
    st.plotly_chart(fig,use_container_width= True)    
    
    



    
    