# Lanzar con streamlit run frontend_gpt.py en el terminal

import backend_asistente_gpt
import streamlit as st
from streamlit_chat import message

st.title("Asistente virtual GPT")
st.write("Realiza consultas especificas de tu base de datos por favor")

if 'mensajes' not in st.session_state:
    st.session_state.mensajes = []

def click():
    if st.session_state.user != '':
        pregunta = st.session_state.user
        respuesta = backend_asistente_gpt.consulta(pregunta)

        # Invierte el orden de los mensajes
        st.session_state.mensajes.insert(0, {"user": False, "content": respuesta})
        st.session_state.mensajes.insert(0, {"user": True, "content": pregunta})

        st.session_state.user = ''

with st.form('my-form'):
    query = st.text_input('¿Qué deseas consultar?:', key='user', help='Pulsa enviar para hacer la consulta')
    submit_button = st.form_submit_button('Consultar', on_click=click)

# Muestra los mensajes en el orden correcto
for mensaje in st.session_state.mensajes:
    if mensaje["user"]:
        message(mensaje["content"], key=str(id(mensaje)), is_user=True)
    else:
        message(mensaje["content"], key=str(id(mensaje)))
