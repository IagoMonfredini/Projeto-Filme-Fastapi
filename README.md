# 🎬 Gerenciador de Filmes

Bem-vindo ao projeto Gerenciador de Filmes, um sistema completo desenvolvido em Python, que une FastAPI e Streamlit para gerenciar um catálogo de filmes.
Com ele, é possível listar, adicionar e atualizar informações sobre filmes de forma prática e interativa.

## 🖼️ Visão Geral

O Gerenciador de Filmes foi criado com o objetivo de demonstrar a integração entre uma API REST (FastAPI) e uma interface web interativa (Streamlit).
A aplicação oferece um sistema CRUD simples e funcional, permitindo que o usuário controle facilmente os dados de filmes em um banco de dados relacional.

## 🧱 Estrutura do Projeto

## 📂 gerenciador-filmes
│
├── app.py → Interface principal em Streamlit (frontend)
├── api.py → API FastAPI com rotas para manipulação dos dados
├── funcao.py → Funções responsáveis pelas operações no banco de dados
├── conexao.py → Configuração e conexão com o banco de dados
├── requirements.txt → Lista de dependências do projeto
└── README.md → Documentação do sistema

## 🧭 Navegação (Interface Streamlit)

O menu lateral do sistema contém as seguintes seções:

## 🎞️ Catálogo – Exibe todos os filmes cadastrados no banco

## ➕ Adicionar Filmes – Permite registrar novos filmes

## ✏️ Atualizar Filmes – Atualiza a avaliação dos filmes existentes

Cada ação é realizada através de botões e campos interativos que se comunicam diretamente com a API FastAPI.

## ⚙️ Tecnologias Utilizadas

Python 3.9+ – Linguagem principal do projeto

FastAPI – Framework backend para criação de APIs REST

Streamlit – Framework frontend para interfaces interativas

Uvicorn – Servidor ASGI para rodar a aplicação FastAPI

Requests – Comunicação entre o frontend e a API

Banco de Dados SQL – Armazenamento dos filmes

psycopg2 / sqlite3 – Driver para conexão com o banco

## 🧩 Endpoints da API
Método	Rota	Descrição
GET	/	Mensagem de boas-vindas
GET	/filmes	Lista todos os filmes cadastrados
POST	/filmes	Adiciona um novo filme
PUT	/filmes/{id_filmes}	Atualiza a avaliação de um filme
(opcional) DELETE	/filmes/{id_filmes}	Exclui um filme do banco

## 📘 Documentação automática da API:

Swagger UI → http://127.0.0.1:8000/docs

Redoc → http://127.0.0.1:8000/redoc

## 🚀 Como Executar o Projeto

Clone o repositório:

git clone https://github.com/seuusuario/gerenciador-filmes.git
cd gerenciador-filmes

Instale as dependências:

pip install -r requirements.txt
