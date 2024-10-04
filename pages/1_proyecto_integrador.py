# pages/2_proyecto_integrador.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Vista de la Base de Datos")  # Título de la página

# Ruta al archivo CSV estático 
ruta_csv = '.\static\Base_datos.csv'

try:
    df = pd.read_csv(ruta_csv)
    st.write("### Datos de la Base de Datos:")
    st.dataframe(df)

    st.write("### Estadísticas descriptivas:")
    st.dataframe(df.describe())

    st.write("### Visualización de Datos:")
    grafico_tipo = st.selectbox("Selecciona el tipo de gráfico:", ["Dispersión", "Histograma", "Box Plot", "Mapa de Calor"])

    if grafico_tipo == "Dispersión":
        x_axis = st.selectbox("Selecciona la columna para el eje X:", df.columns, key='scatter_x_bd')
        y_axis = st.selectbox("Selecciona la columna para el eje Y:", df.columns, key='scatter_y_bd')
        st.line_chart(df[[x_axis, y_axis]])

    elif grafico_tipo == "Histograma":
        columna = st.selectbox("Selecciona la columna para el histograma:", df.columns, key='hist_col_bd')
        st.hist_chart(df[columna])

    elif grafico_tipo == "Box Plot":
        columna = st.selectbox("Selecciona la columna para el Box Plot:", df.columns, key='box_col_bd')
        fig, ax = plt.subplots()
        sns.boxplot(y=df[columna], ax=ax)
        st.pyplot(fig)

    elif grafico_tipo == "Mapa de Calor":
        fig, ax = plt.subplots()
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

except FileNotFoundError:
    st.error(f"No se encontró el archivo CSV en la ruta: {ruta_csv}")
except Exception as e:
    st.error(f"Ocurrió un error al procesar el archivo: {e}")
