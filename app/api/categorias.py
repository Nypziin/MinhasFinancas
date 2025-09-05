from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import SessionLocal
from app.schemas.categoria_schema import CategoriaCreate, CategoriaResponse
from app.services import categoria_service

router = APIRouter(prefix="/categorias", tags=["Categorias"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CategoriaResponse)
def criar_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    return categoria_service.criar_categoria(db, categoria)

@router.get("/", response_model=List[CategoriaResponse])
def listar_categorias(db: Session = Depends(get_db), limite: int=100):
    return categoria_service.listar_categoria(db, limite)


