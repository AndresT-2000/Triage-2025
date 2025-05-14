import streamlit as st

# Título de la aplicación
st.title("Sistema de Clasificación Triage")
st.write("Determina el nivel de atención necesario según la condición del paciente.")

# Entradas del usuario
frecuencia_cardiaca = st.number_input("Frecuencia cardíaca (latidos/min):", min_value=0, value=0)
frecuencia_respiratoria = st.number_input("Frecuencia respiratoria (respiraciones/min):", min_value=0, value=0)
saturacion_oxigeno = st.slider("Saturación de oxígeno (%):", min_value=50, max_value=100, value=100)
temperatura_corporal = st.number_input("Temperatura corporal (°C):", value=36.5)
nivel_dolor = st.slider("Nivel de dolor (0 = Sin dolor, 10 = Máximo dolor):", min_value=0, max_value=10, value=0)

# Otros síntomas
heridas_graves = st.checkbox("Presenta heridas graves o sangrado abundante")
infeccion_severa = st.checkbox("Presenta signos de infección severa (fiebre alta, septicemia)")
dificultad_respiratoria = st.checkbox("Tiene dificultad respiratoria severa")
estado_mental = st.selectbox(
    "Estado mental del paciente:",
    ["Alerta", "Letárgico", "Inconsciente"]
)

# Determinación del nivel de triage
nivel_triage = 5
recomendacion = "El paciente no requiere atención urgente, pero debe seguir un tratamiento adecuado."

if (
    frecuencia_cardiaca > 130 or
    frecuencia_respiratoria > 40 or
    saturacion_oxigeno < 85 or
    temperatura_corporal > 40 or
    dificultad_respiratoria or
    estado_mental == "Inconsciente"
):
    nivel_triage = 1
    recomendacion = "¡El paciente requiere atención inmediata en una sala de urgencias!"

elif (
    110 <= frecuencia_cardiaca <= 130 or
    30 <= frecuencia_respiratoria <= 40 or
    85 <= saturacion_oxigeno <= 90 or
    39 <= temperatura_corporal <= 40 or
    heridas_graves or
    estado_mental == "Letárgico"
):
    nivel_triage = 2
    recomendacion = "El paciente debe recibir atención en menos de 30 minutos."

elif (
    100 <= frecuencia_cardiaca < 110 or
    21 <= frecuencia_respiratoria < 30 or
    91 <= saturacion_oxigeno <= 94 or
    nivel_dolor >= 7 or
    infeccion_severa
):
    nivel_triage = 3
    recomendacion = "El paciente requiere atención urgente en las próximas horas."

elif (
    95 <= frecuencia_cardiaca < 100 or
    16 <= frecuencia_respiratoria <= 20 or
    95 <= saturacion_oxigeno <= 97 or
    37.5 <= temperatura_corporal < 39 or
    nivel_dolor >= 4
):
    nivel_triage = 4
    recomendacion = "El paciente puede esperar atención, pero debe ser evaluado."

# Salida de resultados
st.subheader(f"Nivel de Triage: {nivel_triage}")
st.write(recomendacion)

# Resumen de los datos
st.subheader("Resumen de los Datos del Paciente:")
st.write(f"- Frecuencia cardíaca: {frecuencia_cardiaca} latidos/min")
st.write(f"- Frecuencia respiratoria: {frecuencia_respiratoria} respiraciones/min")
st.write(f"- Saturación de oxígeno: {saturacion_oxigeno}%")
st.write(f"- Temperatura corporal: {temperatura_corporal}°C")
st.write(f"- Nivel de dolor: {nivel_dolor}")
