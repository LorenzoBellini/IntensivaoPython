# Para fazer o Chatbot com IA
# Precisammos de um título
# Precisamos de um input para o usuário digitar a pergunta
# Para cada mensagem que o usuário enviar:
# 1 - Precisamos mostrar a mensagem no chat
# 2 - Pegar a pergunta, e mandar para uma IA
# 3 - Exibir a resposta da IA no chat

# Irei usar Stramlit para criar o backend e o frontend do chatbot
# Vou usar a Groq pois tentei com a OpenAI e Gemini, ambas não deram certo


# Importando as bibliotecas necessárias
import streamlit as st
from groq import Groq


# Criando o modelo de IA
modelo_ia = Groq(api_key="sua_chave_de_api_aqui")


# Título do chatbot
st.write("## Chatbot com IA")

if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []


# Text input para o usuário digitar a pergunta
texto_digitado = st.chat_input("O que gostaria de saber?")


# Armazenar as mensagens do chat em uma lista para exibir no chat
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)


# Envio de mensagens para o chat
if texto_digitado:
    st.chat_message("user").write(texto_digitado)  # Exibe a mensagem do usuário no chat
    mensagem_usuario = {"role": "user", "content": texto_digitado}  # Cria um dicionário para a mensagem do usuário
    st.session_state["lista_mensagens"].append(mensagem_usuario)  # Adiciona a mensagem do usuário à lista de mensagens

    # Resposta da IA
    resposta_ia = modelo_ia.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state["lista_mensagens"],
    )
    texto_resposta_ia = resposta_ia.choices[0].message.content  # Extrai o texto da resposta da IA

    st.chat_message("assistant").write(texto_resposta_ia)  # Exibe a resposta da IA no chat
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}  # Cria um dicionário para a mensagem da IA
    st.session_state["lista_mensagens"].append(mensagem_ia)  # Adiciona a mensagem da IA à lista de mensagens
