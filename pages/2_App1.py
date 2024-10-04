# pages/3_App1.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import StringIO

def descargar_csv(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # Codificar en base64
    href = f'<a href="data:file/csv;base64,{b64}" download="datos_procesados.csv">Descargar CSV Procesado</a>'
    return href

st.title("Análisis de Datos CSV")  # Título de la página

uploaded_file = st.file_uploader("Elige un archivo CSV", type="csv")  # Cargar archivo CSV

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)   # Leer el archivo CSV

        st.write("### Primeras 5 filas del dataset:")
        st.dataframe(df.head())

        st.write("### Información general del DataFrame:")
        buffer = StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

        st.write("### Estadísticas descriptivas de las columnas numéricas:")
        st.dataframe(df.describe())

        # Valores únicos en la columna "País"
        if 'País' in df.columns:
            st.write("### Valores únicos en la columna 'País':")
            valores_unicos_pais = df['País'].unique()
            st.write(valores_unicos_pais)
        else:
            st.warning("La columna 'País' no existe en el DataFrame.")

        # Conteo de ocurrencias en la columna "Género"
        if 'Género' in df.columns:
            st.write("### Cantidad de ocurrencias por 'Género':")
            conteo_genero = df['Género'].value_counts()
            st.bar_chart(conteo_genero)
        else:
            st.warning("La columna 'Género' no existe en el DataFrame.")

        st.write("### Visualización de Datos:")
        grafico_tipo = st.selectbox("Selecciona el tipo de gráfico:", ["Dispersión", "Histograma", "Box Plot", "Mapa de Calor"])

        if grafico_tipo == "Dispersión":
            x_axis = st.selectbox("Selecciona la columna para el eje X:", df.columns, key='scatter_x')
            y_axis = st.selectbox("Selecciona la columna para el eje Y:", df.columns, key='scatter_y')
            st.line_chart(df[[x_axis, y_axis]])

        elif grafico_tipo == "Histograma":
            columna = st.selectbox("Selecciona la columna para el histograma:", df.columns, key='hist_col')
            st.hist_chart(df[columna])

        elif grafico_tipo == "Box Plot":
            columna = st.selectbox("Selecciona la columna para el Box Plot:", df.columns, key='box_col')
            fig, ax = plt.subplots()
            sns.boxplot(y=df[columna], ax=ax)
            st.pyplot(fig)

        elif grafico_tipo == "Mapa de Calor":
            fig, ax = plt.subplots()
            sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)

        # Filtrado de Datos
        st.write("### Filtrar datos:")
        columnas = df.columns.tolist()
        columna_filtrar = st.selectbox("Selecciona la columna para filtrar:", columnas, key='filter_col')
        valor_filtrar = st.text_input(f"Ingresa el valor para filtrar en '{columna_filtrar}':")

        if valor_filtrar:
            # Asegurarse de que la columna existe antes de filtrar
            if columna_filtrar in df.columns:
                df_filtrado = df[df[columna_filtrar].astype(str).str.contains(valor_filtrar, case=False, na=False)]
                st.write(f"#### Datos filtrados por **{columna_filtrar}** que contienen '**{valor_filtrar}**':")
                st.dataframe(df_filtrado)

                # Descargar CSV filtrado
                st.markdown(descargar_csv(df_filtrado), unsafe_allow_html=True)
            else:
                st.warning(f"La columna '{columna_filtrar}' no existe en el DataFrame.")

    except Exception as e:
        st.error(f"Ocurrió un error al procesar el archivo: {e}")
else:
    st.write("Sube un archivo CSV para empezar a analizar.")  # Mostrar información adicional
