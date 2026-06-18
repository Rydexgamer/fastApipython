from fastapi import FastAPI

from routers.alunos import router as alunos_router


# Criamos a aplicação FastAPI.
# O FastAPI já gera a documentação Swagger automaticamente em /docs.
app = FastAPI(
    title="API de Alunos com FastAPI e SQL Server",
    description="Exemplo simples para aula, com FastAPI, SQL Server e rotas REST.",
    version="1.0.0",
)


@app.get("/", tags=["Início"])
def home():
    """
    Endpoint inicial só para mostrar que a API está online.
    """
    return {
        "mensagem": "API no ar com FastAPI.",
        "swagger": "/docs",
        "redoc": "/redoc",
    }


@app.get("/health", tags=["Infra"])
def health_check():
    """
    Endpoint simples para testar se a aplicação subiu.
    """
    return {"status": "ok"}