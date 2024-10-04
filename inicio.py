import streamlit as st
from PIL import Image

# Configura la página
st.set_page_config(page_title="Proyecto Futurista", page_icon="🌌", layout="centered")

# Estilos en CSS para fondo e imagen
st.markdown("""
    <style>
    .futuristic-background {
        background: url(https://firebasestorage.googleapis.com/v0/b/imagenes-e192b.appspot.com/o/graficos.jpg?alt=media&token=4b691a73-9189-472d-b143-41a60440df7d) no-repeat center center fixed;
        background-size: cover;
        padding: 250px;
        border-radius: 15px;
    }
    .title {
        font-family: 'Courier New', monospace;
        color: #00FFEF;
        text-shadow: 0px 0px 10px #00FFEF;
    }
    </style>
""", unsafe_allow_html=True)

# Contenedor principal con fondo futurista
with st.container():
    st.markdown('<div class="futuristic-background">', unsafe_allow_html=True)
    
    # Título con estilo moderno
    st.markdown('<h1 class="title">Bienvenido al Proyecto Integrador</h1>', unsafe_allow_html=True)

    # Descripción del proyecto
    st.markdown("""
    ### Exploración y análisis de datos CSV con un toque del futuro.
    - Sube un archivo CSV para comenzar a analizar.
    - Visualiza gráficos avanzados y personaliza tu análisis.
    """)

    # Cierra el contenedor futurista
    st.markdown('</div>', unsafe_allow_html=True)

