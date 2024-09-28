import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Análisis de Datos CSV")

# Cargar archivo CSV
uploaded_file = st.file_uploader("Elige un archivo CSV", type="csv")

if uploaded_file is not None:
    # Leer el archivo CSV
    df = pd.read_csv(uploaded_file)
    
    # Mostrar las primeras filas del DataFrame
    st.write("Primeras filas del dataset:")
    st.dataframe(df.head())

    # Estadísticas descriptivas
    st.write("Estadísticas descriptivas:")
    st.dataframe(df.describe())

    # Gráficos
    st.write("Gráfico de dispersión:")
    if st.checkbox("Mostrar gráfico de dispersión"):
        x_axis = st.selectbox("Selecciona la columna para el eje X:", df.columns)
        y_axis = st.selectbox("Selecciona la columna para el eje Y:", df.columns)

        st.line_chart(df[[x_axis, y_axis]])

# Mostrar información adicional
st.write("Sube un archivo CSV para empezar a analizar.")
