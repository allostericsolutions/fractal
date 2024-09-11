import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración básica de la aplicación
st.set_page_config(page_title="Museo Virtual Interactivo de Arte Generativo", layout="wide")

# Título principal
st.title("Museo Virtual Interactivo de Arte Generativo")

# Función para mostrar la página de bienvenida
def show_home():
    st.header("¡Bienvenido al Museo Virtual de Arte Generativo!")
    st.write("""
        Explora diversas galerías de arte generativo, ajusta parámetros para personalizar las obras de arte 
        y aprende sobre los algoritmos detrás de estas creaciones. ¡Disfruta de tu visita!
    """)

# Función para mostrar una pieza de arte generativo ajustable
def generate_art(num_lines=50, noise_amplitude=0.5, line_opacity=0.6, cycles=1):
    x = np.linspace(0, 10 * cycles, 100 * cycles)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    for _ in range(num_lines):
        y = np.sin(x) + np.random.normal(scale=noise_amplitude, size=x.shape)
        ax.plot(x, y, alpha=line_opacity)
    plt.close()
    return fig

# Función de galería
def show_gallery():
    st.header("Galería")

    # Parameters for customization
    num_lines = st.slider("Número de líneas", min_value=10, max_value=100, value=50)
    noise_amplitude = st.slider("Amplitud del ruido", min_value=0.1, max_value=1.0, value=0.5)
    line_opacity = st.slider("Opacidad de las líneas", min_value=0.1, max_value=1.0, value=0.6)
    cycles = st.slider("Ciclos de la función seno", min_value=1, max_value=10, value=1)

    fig = generate_art(num_lines, noise_amplitude, line_opacity, cycles)
    st.pyplot(fig)

# Barra lateral para navegación
st.sidebar.title("Navegación")
nav_option = st.sidebar.radio("Ir a", ["Inicio", "Galería"])

# Mostrar la página seleccionada
if nav_option == "Inicio":
    show_home()
elif nav_option == "Galería":
    show_gallery()
