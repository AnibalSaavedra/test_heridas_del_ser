
import streamlit as st
from fpdf import FPDF
from datetime import datetime
import base64
import os

st.set_page_config(page_title="Test de Heridas del Ser", layout="centered")

st.title("🧠 Test Integral de Heridas del Ser")
st.image("logo.png", width=120)
st.markdown("Responde del 1 (nada) al 5 (totalmente de acuerdo).")

afirmaciones = {
    1: "Me cuesta estar solo sin sentir ansiedad.",
    2: "Siento que debo esforzarme para que me amen.",
    3: "Me da vergüenza disfrutar del placer o el cuerpo.",
    4: "Me cuesta confiar plenamente en los demás.",
    5: "Soy muy exigente conmigo mismo.",
}

respuestas = {}
for i in afirmaciones:
    respuestas[i] = st.slider(f"{i}. {afirmaciones[i]}", 1, 5, 3)

if st.button("🔍 Ver Heridas Activas"):
    st.error("🔹 Esta es una vista de ejemplo para el repositorio. Usa la versión extendida para producción.")

st.markdown("---")
st.markdown("📲 [Enviar mensaje por WhatsApp](https://wa.me/56967010107?text=Hola,%20realicé%20el%20test%20de%20Heridas%20del%20Ser%20y%20quiero%20una%20consulta)", unsafe_allow_html=True)
