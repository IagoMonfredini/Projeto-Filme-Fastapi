🎬 Gerenciador de Filmes

O Gerenciador de Filmes é um sistema completo desenvolvido em Python, que permite cadastrar, listar e atualizar filmes através de uma interface amigável construída com Streamlit, conectada a uma API REST desenvolvida com FastAPI.

O objetivo é oferecer um exemplo prático de integração entre frontend e backend, aplicando conceitos de CRUD (Create, Read, Update, Delete) e banco de dados relacional.

🚀 Tecnologias Utilizadas
💻 Frontend

Streamlit → Criação da interface web interativa.

Requests → Comunicação entre o frontend e o backend (API FastAPI).

⚙️ Backend

FastAPI → Criação da API REST.

Uvicorn → Servidor ASGI para rodar o FastAPI.

PostgreSQL / SQLite / outro banco relacional → Armazenamento dos dados.

psycopg2 (ou similar) → Conexão com o banco de dados.

🧩 Estrutura do Projeto
📂 gerenciador_filmes
├── app.py               # Interface Streamlit (frontend)
├── api.py               # API FastAPI (backend)
├── funcao.py            # Funções CRUD e conexão com o banco
├── conexao.py           # Script de conexão ao banco de dados
├── requirements.txt      # Dependências do projeto
└── README.md            # Documentação

🧠 Funcionalidades
🎥 Streamlit (Interface)

O usuário pode:

📖 Visualizar o catálogo de filmes cadastrados.

➕ Adicionar novos filmes informando título, gênero, ano e avaliação.

✏️ Atualizar filmes existentes, modificando a avaliação.

⚙️ FastAPI (API)

Endpoints disponíveis:

Método	Rota	Descrição
GET	/	Mensagem de boas-vindas
GET	/filmes	Lista todos os filmes
POST	/filmes	Adiciona um novo filme
PUT	/filmes/{id_filmes}	Atualiza a avaliação de um filme
DELETE	/filmes/{id_filmes}	(opcional) Exclui um filme do banco

📘 Documentação automática da API:

Swagger UI → http://127.0.0.1:8000/docs

Redoc → http://127.0.0.1:8000/redoc

⚙️ Como Executar o Projeto
1️⃣ Clonar o repositório
git clone https://github.com/usuario/gerenciador-filmes.git
cd gerenciador-filmes

2️⃣ Instalar dependências
pip install -r requirements.txt

