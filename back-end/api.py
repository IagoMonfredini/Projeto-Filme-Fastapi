from fastapi import FastAPI
from funcao import inserir_filmes, listar_filmes, atualizar_filmes, deletar_filmes

#Rodar o fastapi
# python -m uvicorn api.py: app -reload

#Testar api Fastapi
# /docs > Documentação Swagger
# /redoc > Documentação redoc

#Iniciar a fastapi
app = FastAPI(title="Gerenciador de filmes")

#GET = Pegar / Listar
#POST = Criar / Enviar
#PUT = Atualizar
#DELETE = Deletar 

@app.get("/")
def home(): 
    return {"mensagem": "Quero chocolate"}

@app.post("/filmes")
def criar_filmes(titulo: str, genero: str, ano: int, avaliacao: float):
    inserir_filmes(titulo, genero, ano, avaliacao)
    return {"mensagem": "Filme adicionado com sucesso!"}