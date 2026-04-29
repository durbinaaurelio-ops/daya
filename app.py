import streamlit as st
import random

st.set_page_config(page_title="Trivia Villanas Disney", page_icon="👑")

st.title("👑 Trivia: Villanas de Disney")
st.write("Responde correctamente las 5 preguntas 🧙‍♀️")

# Preguntas
questions = [
    {
        "question": "¿Cómo se llama la villana de La Sirenita?",
        "options": ["Úrsula", "Maléfica", "Cruella", "Yzma"],
        "answer": "Úrsula"
    },
    {
        "question": "¿Qué villana puede transformarse en dragón?",
        "options": ["Maléfica", "Gothel", "Reina Malvada", "Cruella"],
        "answer": "Maléfica"
    },
    {
        "question": "¿Quién es la villana de 101 Dálmatas?",
        "options": ["Cruella de Vil", "Úrsula", "Yzma", "Madre Gothel"],
        "answer": "Cruella de Vil"
    },
    {
        "question": "¿Qué villana envenena una manzana?",
        "options": ["Reina Malvada", "Maléfica", "Gothel", "Úrsula"],
        "answer": "Reina Malvada"
    },
    {
        "question": "¿Qué villana secuestra a Rapunzel?",
        "options": ["Madre Gothel", "Cruella", "Yzma", "Maléfica"],
        "answer": "Madre Gothel"
    }
]

score = 0

user_answers = []

# Mostrar preguntas con opciones aleatorias
for i, q in enumerate(questions):
    st.subheader(f"Pregunta {i+1}")
    
    options = q["options"].copy()
    random.shuffle(options)
    
    answer = st.radio(q["question"], options, key=i)
    user_answers.append(answer)

# Botón para evaluar
if st.button("Ver resultados"):
    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            score += 1
    
    st.write(f"Tu puntaje: {score}/5")
    
    if score == 5:
        st.success("¡Perfecto! 🎉 Conoces a todas las villanas")
        st.balloons()  # animación 🎈
    elif score >= 3:
        st.info("¡Nada mal! 😄")
    else:
        st.warning("Sigue intentando 😅")
