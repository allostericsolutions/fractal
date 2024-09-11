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

# Función para mostrar una pieza de arte generativo simple
def generate_art(num_lines=50):
    x = np.linspace(0, 10, 100)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    for _ in range(num_lines):
        y = np.sin(x) + np.random.normal(scale=0.5, size=x.shape)
        ax.plot(x, y, alpha=0.6)
    plt.close()
    return fig

# Función de galería
def show_gallery():
    st.header("Galería")
    num_lines = st.slider("Número de líneas", min_value=10, max_value=100, value=50)
    fig = generate_art(num_lines)
    st.pyplot(fig)

# Barra lateral para navegación
st.sidebar.title("Navegación")
nav_option = st.sidebar.radio("Ir a", ["Inicio", "Galería"])

# Mostrar la página seleccionada
if nav_option == "Inicio":
    show_home()
elif nav_option == "Galería":
    show_gallery()

if __name__ == "__main__":
    st.experimental_rerun()
