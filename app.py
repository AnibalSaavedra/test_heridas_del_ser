
import streamlit as st
from fpdf import FPDF
from datetime import datetime
import base64
import os

st.set_page_config(page_title="Test de Heridas del Ser", layout="centered")

st.title("🧠 Test Integral de Heridas del Ser")
st.image("logo.png", width=120)
st.markdown("Responde cada afirmación del 1 (nada) al 5 (totalmente de acuerdo). Al finalizar verás tus heridas activas y recibirás recomendaciones.")

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
    "Abandono": "Dependencia emocional, miedo a la soledad, ansiedad de separación.",
    "Rechazo": "Autoexigencia, necesidad de aprobación, miedo a no ser suficiente.",
    "Humillación": "Vergüenza corporal, culpa, dificultad para disfrutar.",
    "Traición": "Control, desconfianza, celos, rigidez.",
    "Injusticia": "Frialdad, perfeccionismo, autoexigencia extrema.",
    "Falta de propósito": "Vacío existencial, apatía, pérdida de rumbo.",
    "Desarraigo": "Sensación de no pertenecer, dificultad para establecer raíces.",
    "Invisibilidad": "Sensación de no importar, baja autoestima, represión emocional.",
    "Transgeneracional": "Cargas familiares no conscientes, patrones repetidos.",
    "Disociación": "Ansiedad, desconexión del cuerpo, crisis de identidad.",
    "Carencia": "Sensación de no merecer, dificultad para recibir.",
    "Duelo": "Tristeza profunda, apego al pasado, miedo a nuevos vínculos.",
    "Identidad": "Confusión personal, doble vida, represión.",
    "Amor no correspondido": "Dependencia afectiva, dolor emocional, idealización.",
    "Mixtas": "Emociones mezcladas, patrones repetitivos, caos interno."
}

respuestas = {}
for i in range(1, 21):
    respuestas[i] = st.slider(f"{i}. {afirmaciones[i]}", 1, 5, 3)

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
            st.error(f"🔹 {h} ({estado} - {pct}%)

{explicaciones[h]}")
        st.session_state.heridas_activas = heridas_activas
    else:
        st.success("🎉 No hay heridas activas detectadas. ¡Sigue cuidándote emocionalmente!")

if "heridas_activas" in st.session_state and st.button("📄 Descargar Informe PDF"):
    class PDF(FPDF):
        def header(self):
            self.set_font("Arial", "B", 12)
            self.cell(0, 10, "Informe de Heridas del Ser", 0, 1, "C")
        def chapter(self, h, estado, pct, explicacion):
            self.set_font("Arial", "B", 12)
            self.cell(0, 10, f"{h} ({estado} - {pct}%)", 0, 1)
            self.set_font("Arial", "", 11)
            self.multi_cell(0, 8, explicacion)
            self.ln()
        def footer(self):
            self.set_y(-20)
            self.set_font("Arial", "I", 10)
            self.cell(0, 10, "Informe generado por Anibal Saavedra – Biotecnólogo MIB", 0, 0, "C")

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 10, f"Fecha: {datetime.now().strftime('%d/%m/%Y')}", 0, 1)
    for h, (estado, pct) in st.session_state.heridas_activas.items():
        pdf.chapter(h, estado, pct, f"- Descripción: {explicaciones[h]}\n- Estado: {estado}\n- Porcentaje: {pct}%")
    pdf.output("informe_heridas.pdf")

    with open("informe_heridas.pdf", "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="informe_heridas.pdf">📥 Haz clic aquí para descargar tu informe PDF</a>'
        st.markdown(href, unsafe_allow_html=True)

    os.remove("informe_heridas.pdf")

if "heridas_activas" in st.session_state:
    st.markdown("---")
    st.markdown("📲 ¿Deseas agendar una consulta personal?")
    mensaje = "Hola Anibal, realicé el test de Heridas del Ser y quiero agendar una consulta personalizada."
    url_whatsapp = f"https://wa.me/56967010107?text={mensaje.replace(' ', '%20')}"
    st.markdown(f"[💬 Enviar mensaje por WhatsApp]({url_whatsapp})", unsafe_allow_html=True)
