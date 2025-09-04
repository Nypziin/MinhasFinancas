from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api import gastos, enum
from app.core.database import Base, engine
from app.models import gasto, categoria

app = FastAPI()

# Servir os arquivos estáticos (html, css, js, imagens)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def read_index():
    return FileResponse("frontend/index.html")

app.include_router(gastos.router)
app.include_router(enum.router)