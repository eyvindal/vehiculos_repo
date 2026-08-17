#Este es el codigo de la app web

import pandas as pd
import streamlit as st
import plotly.graph_objects as go

#se carga el archivo con los datos
df = pd.read_csv("python/sprint7_tf/smartphones_repo/data/vehicles_us.csv")

#encabezado de la aplicacion
st.title("Información del odómetro:")
st.write("A continuación usted encontrará información relevante recopilada sobre el millaje mostrado en los odómetros de los vehículos disponibles.")

st.header("Distribución del millaje en odómetro")

#creo un boton que al hacer clic construye un histograma
hist_button = st.button('Construir histograma')

#codigo para que imprima un histograma
if hist_button:
    # mensaje de la aplicación
    st.write('Este es un histograma que muestra la distribución del millaje en millones de millas de los vehículos disponibles.')

    # histograma utilizando plotly.graph_objects
    fig = go.Figure(data=[go.Histogram(x=df['odometer'])])
    fig.update_layout(title_text='Distribución del millaje')

    # se imprime el grafico en la aplicación
    st.plotly_chart(fig, use_container_width=True)


st.header("Relación entre el millaje y el precio del vehículo")

#creo un boton que al hacer clic construye un gráfico de dispersion
disp_button = st.button('Construir gráfico de dispersión')

#codigo para que imprima un gráfico de dispersion
if disp_button:
    # mensaje en la aplicación
    st.write('Este es un gráfico de dispersion que relaciona el millaje en millones de millas con el precio de cada vehículo disponible.')

    # grafico de dispersion utilizando plotly.graph_objects
    fig = go.Figure(data=[go.Scatter(
                        x=df['odometer'], 
                        y=df["price"],
                        mode='markers', 
                        marker=dict(size=12, color='blue', opacity=0.8))])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Relación entre el millaje y el precio del vehículo')

    # se imprime el grafico en la aplicación
    st.plotly_chart(fig, use_container_width=True)