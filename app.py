
import streamlit as st
from fpdf import FPDF
from datetime import datetime
import base64
import os

st.set_page_config(page_title="Test de Heridas del Ser", layout="centered")

st.title("🧠 Test Integral de Heridas del Ser")
st.image("logo.png", width=120)
st.markdown("""
Este test te ayudará a **identificar heridas emocionales** que influyen en tu bienestar actual.  
**Lee cada afirmación con calma** y responde del 1 al 5 según cuánto te identifiques:

- 1: No me representa  
- 3: A veces me ocurre  
- 5: Me ocurre frecuentemente

📘 Si no entiendes alguna afirmación, haz clic en el botón `Explicar` para recibir una aclaración sencilla que te ayudará a comprender mejor.
""")

heridas = {
    "Abandono": [1, 16],
    "Rechazo": [2, 18],
    "Humillación": [3, 15],
    "Traición": [4],
    "Injusticia": [5],
    "Falta de propósito": [6],
    "Desarraigo": [7],
    "Invisibilidad": [8],
    "Transgeneracional": [9, 20],
    "Disociación": [10, 17],
    "Carencia": [11],
    "Duelo": [12],
    "Identidad": [13],
    "Amor no correspondido": [14],
    "Mixtas": [19]
}

afirmaciones = {
    1: "Me cuesta mucho estar solo sin sentir ansiedad.",
    2: "Siento que debo esforzarme para que me amen.",
    3: "Me da vergüenza disfrutar del placer o el cuerpo.",
    4: "Me cuesta confiar plenamente en los demás.",
    5: "Soy muy exigente conmigo mismo, nunca es suficiente.",
    6: "A veces siento que nada tiene sentido.",
    7: "Me siento como si no perteneciera a ningún lugar.",
    8: "Siento que no soy visto, aunque esté presente.",
    9: "Tengo recuerdos o sensaciones que no son míos.",
    10: "Me cuesta recordar partes de mi infancia.",
    11: "Me cuesta mucho recibir ayuda o afecto.",
    12: "Me duele recordar a alguien que se fue.",
    13: "Siento que tengo que demostrar constantemente mi valor.",
    14: "Me afecta cuando alguien no me ama como yo espero.",
    15: "Me siento culpable por desear cosas buenas para mí.",
    16: "Siento que algo malo puede pasar en cualquier momento.",
    17: "Me cuesta disfrutar del presente, vivo con miedo al futuro.",
    18: "Me paralizo cuando me critican o me rechazan.",
    19: "A veces me comporto como si no tuviera edad emocional.",
    20: "Siento que cargo con los dolores de mi familia."
}

explicaciones = {
    1: "¿Te sientes inquieto o nervioso cuando no hay nadie contigo?",
    2: "¿Sientes que necesitas hacer cosas para que otros te valoren?",
    3: "¿Te incomoda sentir placer físico o expresarte corporalmente?",
    4: "¿Te cuesta abrir tu mundo interior por miedo a ser herido?",
    5: "¿Sientes que debes rendir más aunque ya haces mucho?",
    6: "¿Te preguntas a veces para qué estás aquí o qué sentido tiene tu vida?",
    7: "¿Te sientes fuera de lugar incluso con gente cercana?",
    8: "¿Sientes que no notan tu presencia o tu esfuerzo?",
    9: "¿Tienes emociones o sueños que parecen no ser tuyos?",
    10: "¿Hay momentos de tu infancia que simplemente no recuerdas?",
    11: "¿Te cuesta aceptar ayuda o muestras de cariño?",
    12: "¿Recuerdas con tristeza o dolor a alguien que ya no está?",
    13: "¿Sientes que debes probar constantemente que vales?",
    14: "¿Te afecta mucho si alguien no responde a tu amor?",
    15: "¿Te sientes mal por disfrutar o darte gustos personales?",
    16: "¿Tienes la sensación de que algo malo está por pasar?",
    17: "¿Sientes que no puedes disfrutar el presente por pensar en lo que viene?",
    18: "¿Te bloqueas cuando sientes rechazo o crítica?",
    19: "¿A veces reaccionas como si fueras un niño o adolescente?",
    20: "¿Sientes que arrastras emociones que no son tuyas?"
}

respuestas = {}
for i in range(1, 21):
    col1, col2 = st.columns([5, 1])
    with col1:
        respuestas[i] = st.slider(f"{i}. {afirmaciones[i]}", 1, 5, 3, key=f"slider_{i}")
    with col2:
        if st.button("Explicar", key=f"help_{i}"):
            st.info(explicaciones[i])

if st.button("🔍 Ver Heridas Activas"):
    heridas_activas = {}
    for herida, items in heridas.items():
        total = sum([respuestas[i] for i in items])
        maximo = len(items) * 5
        porcentaje = round((total / maximo) * 100)
        if porcentaje >= 70:
            heridas_activas[herida] = ("Activa intensa", porcentaje)
        elif porcentaje >= 40:
            heridas_activas[herida] = ("Activa moderada", porcentaje)

    if heridas_activas:
        st.subheader("💔 Tus Heridas Activas")
        for h, (estado, pct) in heridas_activas.items():
            st.error(f"🔹 {h} ({estado} - {pct}%)")
        st.success("📄 Puedes solicitar ayuda profesional si te sientes identificado.")
    else:
        st.success("🎉 No hay heridas activas detectadas. ¡Sigue cuidándote emocionalmente!")

st.markdown("---")
st.markdown("¿Deseas conversar con un terapeuta?")
if st.button("💬 Contactar vía WhatsApp"):
    js = "window.open('https://wa.me/56967010107','_blank')"
    st.components.v1.html(f"<script>{js}</script>", height=0)
