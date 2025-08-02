
import streamlit as st
from fpdf import FPDF
from datetime import datetime
import base64
import os

st.set_page_config(page_title="Test de Heridas del Ser", layout="centered")

st.title("🧠 Test Integral de Heridas del Ser")
st.image("logo.png", width=120)
st.markdown(
    "Este test te ayudará a identificar heridas emocionales que pueden influir en tu bienestar actual. "
    "**Lee atentamente cada afirmación** y responde del 1 al 5 según cuánto te identifiques:

"
    "- 1: No me identifico en absoluto
"
    "- 3: A veces me pasa
"
    "- 5: Me ocurre con mucha frecuencia

"
    "💡 Si tienes dudas sobre el significado de alguna afirmación, puedes presionar el botón de ayuda al lado para recibir una breve explicación."
)

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

ayudas = {
    1: "Ansiedad al estar solo puede mostrar miedo a ser abandonado.",
    2: "Buscar amor esforzándote muestra necesidad de validación.",
    3: "Vergüenza corporal puede ocultar una herida de humillación.",
    4: "La dificultad para confiar puede venir de traiciones pasadas.",
    5: "Ser exigente puede ser resultado de injusticia vivida.",
    6: "Sensación de vacío es una señal de pérdida de propósito.",
    7: "No sentir pertenencia puede indicar desarraigo o exclusión.",
    8: "Sentirse invisible suele relacionarse con heridas infantiles.",
    9: "Cargar memorias que no son tuyas puede ser transgeneracional.",
    10: "Desconexión con la infancia indica posibles bloqueos.",
    11: "Dificultad en recibir amor habla de heridas de carencia.",
    12: "Dolor por pérdidas puede mostrar duelo no resuelto.",
    13: "Demostrar tu valor puede ocultar inseguridad de identidad.",
    14: "Sufrir por amor no correspondido muestra dependencia emocional.",
    15: "La culpa al disfrutar puede estar asociada a humillación.",
    16: "Esperar lo peor es propio del miedo al abandono.",
    17: "No disfrutar el presente es típico de disociación emocional.",
    18: "El rechazo paralizante es una herida del yo profundo.",
    19: "Inmadurez emocional puede ser resultado de heridas mixtas.",
    20: "Dolor heredado sin vivirlo es carga transgeneracional."
}

respuestas = {}
for i in range(1, 21):
    col1, col2 = st.columns([5, 1])
    with col1:
        respuestas[i] = st.slider(f"{i}. {afirmaciones[i]}", 1, 5, 3, key=f"slider_{i}")
    with col2:
        if st.button("?", key=f"help_{i}"):
            st.info(ayudas[i])

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
            st.error(f"🔹 {h} ({estado} - {pct}%)\n\n{ayudas[list(afirmaciones.keys())[list(heridas[h])[0] - 1]]}")
        st.session_state.heridas_activas = heridas_activas
    else:
        st.success("🎉 No hay heridas activas detectadas. ¡Sigue cuidándote emocionalmente!")
