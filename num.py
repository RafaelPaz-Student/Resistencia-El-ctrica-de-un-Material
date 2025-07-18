import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Calculadora de Resistencia Eléctrica de un Material")

st.markdown("""
Usa la fórmula:

> **R = ρ · (L / A)**

Donde:
- **R** = Resistencia (Ω)
- **ρ** = Resistividad del material (Ω·m)
- **L** = Longitud del conductor (m)
- **A** = Área de la sección transversal (m²)
""")

# Entradas del usuario
resistividad = st.number_input("Resistividad del material (Ω·m)", min_value=0.0, value=1.68e-8)
longitud = st.number_input("Longitud del conductor (m)", min_value=0.0, value=1.0)
area = st.number_input("Área de la sección transversal (m²)", min_value=0.0000001, value=1e-6, format="%.8f")

# Cálculo de la resistencia
if area > 0:
    resistencia = resistividad * (longitud / area)
    st.success(f"✅ Resistencia del material: **{resistencia:.6f} Ω**")
else:
    st.error("❌ El área debe ser mayor que cero.")

# Gráfico opcional
if st.checkbox("Mostrar gráfico de resistencia vs longitud"):
    longitudes = np.linspace(0.1, 10, 100)
    resistencias = resistividad * (longitudes / area)

    fig, ax = plt.subplots()
    ax.plot(longitudes, resistencias, color='blue')
    ax.set_xlabel("Longitud (m)")
    ax.set_ylabel("Resistencia (Ω)")
    ax.set_title("Resistencia vs Longitud")
    ax.grid(True)

    st.pyplot(fig)

