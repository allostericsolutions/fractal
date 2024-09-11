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
def generate_art(num_lines=50, noise_amplitude=0.5, line_opacity=0.6, cycles=1, 
                 freq=1, amplitude=1, color='blue', linewidth=1, linestyle='-', 
                 bgcolor='white', show_grid=True, y_limit=5, y_threshold=2, phase_randomness=0):
    x = np.linspace(0, 10 * cycles, 100 * cycles)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_facecolor(bgcolor)
    if show_grid:
        ax.grid(True)
    for _ in range(num_lines):
        phase_shift = np.random.uniform(-phase_randomness, phase_randomness)
        y = amplitude * np.sin(freq * x + phase_shift) + np.random.normal(scale=noise_amplitude, size=x.shape)
        # Apply y_threshold
        y = np.where(np.abs(y) > y_threshold, np.sign(y) * y_threshold, y)
        ax.plot(x, y, alpha=line_opacity, color=color, linewidth=linewidth, linestyle=linestyle)
    ax.set_ylim(-y_limit, y_limit)
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
    freq = st.slider("Frecuencia de la función seno", min_value=0.1, max_value=5.0, value=1.0)
    amplitude = st.slider("Amplitud de la función seno", min_value=0.1, max_value=5.0, value=1.0)
    color = st.color_picker("Color de la línea", value='#0000FF')
    linewidth = st.slider("Ancho de la línea", min_value=0.5, max_value=5.0, value=1.0)
    linestyle = st.selectbox("Estilo de la línea", options=['-', '--', '-.', ':'])
    bgcolor = st.color_picker("Color de fondo", value='#FFFFFF')
    show_grid = st.checkbox("Mostrar grilla", value=True)
    y_limit = st.slider("Límite en el eje Y", min_value=0, max_value=10, value=5)
    y_threshold = st.slider("Protección contra línea de alto valor (umbral)", min_value=0.5, max_value=10.0, value=2.0)
    phase_randomness = st.slider("Aleatoriedad de la fase", min_value=0.0, max_value=3.14, value=0.0)

    fig = generate_art(num_lines, noise_amplitude, line_opacity, cycles, freq, amplitude, color, linewidth, linestyle, bgcolor, show_grid, y_limit, y_threshold, phase_randomness)
    st.pyplot(fig)

# Barra lateral para navegación
st.sidebar.title("Navegación")
nav_option = st.sidebar.radio("Ir a", ["Inicio", "Galería"])

# Mostrar la página seleccionada
if nav_option == "Inicio":
    show_home()
elif nav_option == "Galería":
    show_gallery()
