pip install streamlit

import streamlit as st
import random

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="💌 Mensagem do Dia",
    page_icon="💖",
    layout="centered"
)

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #cceeff, #e6f7ff);
        font-family: 'Comic Sans MS', cursive;
    }

    .stButton button {
        background-color: #FF6F61;
        color: white;
        border-radius: 15px;
        padding: 0.8em 1.5em;
        font-size: 1.2em;
        font-weight: bold;
        border: none;
    }

    .message-box {
        background-color: #fffbe6;
        border: 2px dashed #ffc107;
        padding: 30px;
        border-radius: 20px;
        font-size: 1.5em;
        text-align: center;
        color: #333;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- MASCOTE FOFO ---
st.image("https://i.imgur.com/dGB6cWq.png", width=120)  # Mascote simpático

# --- TÍTULO E DESCRIÇÃO ---
st.title("💌 Mensagem do Dia")
st.markdown("Escolha uma categoria e receba uma mensagem cheia de carinho ✨")

# --- CATEGORIAS DE MENSAGEM ---
categoria = st.radio("Escolha a categoria:", ["Infantil", "Família", "Geral"], horizontal=True)

# --- LISTAS DE MENSAGENS ---
mensagens_infantis = [
    "Você é uma estrelinha brilhando no céu do aprendizado! 🌟",
    "Aprender pode ser divertido, assim como brincar! 🎲",
    "Cada passo seu é uma conquista. Continue assim! 🐾",
    "Seu sorriso já é uma vitória! 😄",
    "Você pode voar alto com seus sonhos! 🦋"
]

mensagens_familia = [
    "A educação começa com amor em casa. 🏡",
    "Família unida é a base para todo crescimento. 🤝",
    "Seu apoio faz toda a diferença na vida da criança. 💖",
    "Cada momento em família é um presente. 🎁",
    "Amar, cuidar e ensinar: vocês estão fazendo um lindo trabalho. 🌷"
]

mensagens_geral = [
    "Errar é aprender de outro jeito. Continue tentando! 💪",
    "Seu esforço vale ouro! 🏅",
    "Com carinho e paciência, tudo se aprende. 🧠💗",
    "Educar é um ato de amor e esperança. 🌟",
    "Você está ajudando a construir um mundo melhor. 🌍"
]

# --- ESCOLHER LISTA CERTA ---
if categoria == "Infantil":
    mensagens = mensagens_infantis
elif categoria == "Família":
    mensagens = mensagens_familia
else:
    mensagens = mensagens_geral

# --- BOTÃO PARA GERAR MENSAGEM ---
if st.button("Nova Mensagem 💖"):
    mensagem = random.choice(mensagens)
    st.markdown(f"<div class='message-box'>{mensagem}</div>", unsafe_allow_html=True)
