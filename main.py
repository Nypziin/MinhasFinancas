from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import  Jinja2Templates
from app.api import gastos

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

@app.get("/ping")
async def ping():
    return {"ping": "pong"}

app.include_router(gastos.router)