from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api import gastos, enum

app = FastAPI()

# Servir os arquivos estáticos (html, css, js, imagens)
app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.get("/ping")
async def ping():
    return {"ping": "pong"}

@app.get("/")
def read_index():
    return FileResponse("frontend/index.html")

@app.get("/minha-api")
def minha_api():
    return {"mensagem": "Olá do backend FastAPI!"}

app.include_router(gastos.router)
app.include_router(enum.router)