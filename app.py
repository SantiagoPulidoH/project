import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv(
    r'C:\Users\santi\sprint_7\project\vehicles_us.csv')  # leer los datos

st.header('Bienvenido a la primera pagina web de Santiago')

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

hist_button = st.button('Construir grafico de dispersion')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
