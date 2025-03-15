import requests 
import streamlit as st
from streamlit_lottie import st_lottie


st.image("img/pattern2.jpg")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f8ae5c;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("<h1 style='text-align: center; color: #226624'>Unidades</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
       /* Estilo do botão geral */
       .botao {
          margin-inline: 25%;
          display: flex; /* Alinha o conteúdo do botão */
          align-items: center; /* Centraliza o texto e a imagem verticalmente */
          justify-content: center; /* Centraliza o conteúdo horizontalmente */
          background-color: #4CAF50;
          border: none;
          border-radius: 30px; /* Torna o botão arredondado */
          padding: 10px 20px;
          cursor: pointer;
          color: white;
          font-size: 30px;
          transition: transform 0.2s, box-shadow 0.2s;
       }

       /* Estilo para botão alinhado à direita */
       .botao_direita {
          float: right;
       }

       

       /* Animação ao passar o mouse */
       .botao:hover {
          transform: scale(1.05); /* Aumenta levemente o botão */
          box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2); /* Adiciona uma sombra */
       }

       /* Remove borda ao focar */
       .botao:focus {
          outline: none;
       }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML dos botões
button_cotidiano = """
<button class="botao botao_direita">Cotidiano</button>
"""
button_corpo = """
<button class="botao ">Corpo</button>
"""
button_animais = """
<button class="botao botao_direita">Animais</button>
"""
button_comida = """
<button class="botao ">Comida</button>
"""
button_continuar = """
<button class="botao botao_direita .botao_continuar">Continuar</button>
"""

# Renderizando botões no Streamlit
st.markdown(button_cotidiano, unsafe_allow_html=True)
st.markdown(button_corpo, unsafe_allow_html=True)
st.markdown(button_animais, unsafe_allow_html=True)
st.markdown(button_comida, unsafe_allow_html=True)
st.markdown(button_continuar, unsafe_allow_html=True)

st.image("img/pattern2.jpg")

