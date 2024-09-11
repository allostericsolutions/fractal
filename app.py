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
                 freq=1, amplitude=1, color_palette=['#0000FF'], linewidth=1, linestyle='-',
                 bgcolor='white', show_grid=False, y_limit=5, y_threshold=2, phase_randomness=0, x_limit=10):
    
    x = np.linspace(0, x_limit * cycles, 100 * cycles)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_facecolor(bgcolor)
    ax.axis('off')  # Desactiva los ejes
    if show_grid:
        ax.grid(True)
    
    num_colors = len(color_palette)
    
    for i in range(num_lines):
        phase_shift = np.random.uniform(-phase_randomness, phase_randomness)
        y = amplitude * np.sin(freq * x + phase_shift) + np.random.normal(scale=noise_amplitude, size=x.shape)
        # Apply y_threshold
        y = np.where(np.abs(y) > y_threshold, np.sign(y) * y_threshold, y)
        ax.plot(x, y, alpha=line_opacity, color=color_palette[i % num_colors], linewidth=linewidth, linestyle=linestyle)
        
    ax.set_ylim(-y_limit, y_limit)
    plt.close()
    return fig

# Función para mostrar fractales
def generate_fractal(iterations=100, zoom=1.0, pan_x=0.0, pan_y=0.0):
    # Set the range and resolution of the complex plane
    x_min, x_max = -2.0 / zoom + pan_x, 2.0 / zoom + pan_x
    y_min, y_max = -2.0 / zoom + pan_y, 2.0 / zoom + pan_y
    width, height = 800, 800
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C)
    M = np.zeros(C.shape, dtype=bool)
    for i in range(iterations):
        Z = Z**2 + C
        M = np.logical_or(M, np.abs(Z) > 2)
    
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(M, extent=[x_min, x_max, y_min, y_max], cmap='inferno')
    ax.axis('off')  # Desactiva los ejes
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
    colors = st.beta_expander("Selecciona los colores de las líneas")
    color_palette = colors.multiselect("Colores de las líneas", options=['#0000FF', '#FF0000', '#00FF00', '#FFFF00', '#FF00FF', '#00FFFF', '#000000'], default=['#0000FF'])
    linewidth = st.slider("Ancho de la línea", min_value=0.5, max_value=5.0, value=1.0)
    linestyle = st.selectbox("Estilo de la línea", options=['-', '--', '-.', ':'])
    bgcolor = st.color_picker("Color de fondo", value='#FFFFFF')
    show_grid = st.checkbox("Mostrar grilla", value=False)
    y_limit = st.slider("Límite en el eje Y", min_value=0, max_value=10, value=5)
    y_threshold = st.slider("Protección contra línea de alto valor (umbral)", min_value=0.5, max_value=10.0, value=2.0)
    phase_randomness = st.slider("Aleatoriedad de la fase", min_value=0.0, max_value=3.14, value=0.0)
    x_limit = st.slider("Límite en el eje X", min_value=1, max_value=20, value=10)

    fig = generate_art(num_lines, noise_amplitude, line_opacity, cycles, freq, amplitude, color_palette, linewidth, linestyle, bgcolor, show_grid, y_limit, y_threshold, phase_randomness, x_limit)
    st.pyplot(fig)

# Función de fractales
def show_fractals():
    st.header("Fractales")

    # Parameters for customization
    iterations = st.slider("Número de iteraciones", min_value=10, max_value=500, value=100)
    zoom = st.slider("Zoom", min_value=0.1, max_value=10.0, value=1.0)
    pan_x = st.slider("Pan (X)", min_value=-2.0, max_value=2.0, value=0.0)
    pan_y = st.slider("Pan (Y)", min_value=-2.0, max_value=2.0, value=0.0)

    fig = generate_fractal(iterations, zoom, pan_x, pan_y)
    st.pyplot(fig)

# Barra lateral para navegación
st.sidebar.title("Navegación")
nav_option = st.sidebar.radio("Ir a", ["Inicio", "Galería", "Fractales"])

# Mostrar la página seleccionada
if nav_option == "Inicio":
    show_home()
elif nav_option == "Galería":
    show_gallery()
elif nav_option == "Fractales":
    show_fractals()
