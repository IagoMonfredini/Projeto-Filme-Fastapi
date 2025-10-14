import streamlit as st
import requests

#URL da API FastAPI
API_URL = "http://127.0.0.1:8000/"

# Roda o streamlit
#   python -m streamlit run app.py

st.set_page_config(page_title="Gerenciador de filmes", page_icon="🎬")
st.title("🎥Gerenciador de filmes")

#Menu lateral

menu = st.sidebar.radio("Navegação", {"Catalogo", "Adicionar filmes"})

if menu == "Catalogo":
    st.subheader("Todos os filmes disponiveis")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if filmes:
            for linha in filmes:
                st.write(f"**{filmes['titulo']}**")
    else:
        st.error("Erro ao acessar a API")