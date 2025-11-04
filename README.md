🛒 Gerenciador de Produtos

Este projeto é uma aplicação completa para gestão de estoque, unindo um backend em FastAPI e um frontend em Streamlit.
O sistema permite listar, adicionar, atualizar e deletar produtos, conectando-se via requisições HTTP entre as duas camadas.

🚀 Tecnologias Utilizadas
🔹 Backend (API)

FastAPI
 → Criação da API REST.

Python → Linguagem principal.

Uvicorn → Servidor ASGI para executar o FastAPI.

🔹 Frontend (Interface)

Streamlit
 → Interface gráfica interativa e fácil de usar.

Requests → Comunicação entre o frontend e a API.

📂 Estrutura do Projeto
📦 projeto_estoque
├── api.py                # Backend FastAPI
├── app.py                # Frontend Streamlit
├── funcao.py             # Funções auxiliares (CRUD no banco de dados)
├── requirements.txt       # Dependências do projeto
└── README.md             # Documentação do projeto

⚙️ Funcionalidades
🧩 FastAPI (Backend)

GET / → Mensagem de boas-vindas.

POST /produtos → Adiciona um novo produto ao estoque.

GET /produtos → Lista todos os produtos cadastrados.

PUT /produtos/{id_produto} → Atualiza informações de um produto existente.

DELETE /produtos/{id_produto} → Exclui um produto do estoque.

📘 Documentação automática da API:

Swagger UI → http://127.0.0.1:8000/docs

Redoc → http://127.0.0.1:8000/redoc

💻 Streamlit (Frontend)

Interface interativa com 4 seções principais:

Estoque: Visualiza todos os produtos cadastrados.

Registrar Produto: Adiciona novos produtos.

Atualizar Produto: Edita dados de produtos existentes.

Deletar Produto: Remove produtos do sistema.

🔧 Como Executar o Projeto
1️⃣ Clonar o repositório
git clone https://github.com/usuario/gerenciador-produtos.git
cd gerenciador-produtos

2️⃣ Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate   # Linux/Mac

3️⃣ Instalar dependências
pip install -r requirements.txt
