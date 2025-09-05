from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.categoria_schema import CategoriaCreate
from app.repositories import categoria_repository
from app.models.categoria import Categoria
from typing import List

def criar_categoria(db: Session, categoria: CategoriaCreate) -> Categoria:
    nome = categoria.nome_categoria
    if categoria_repository.categoria_por_id(db, nome):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Categoria já existe")
    return categoria_repository.criar_categorias(db, categoria)

def listar_categoria(db: Session, limite: int = 100) -> List[Categoria]:
    return categoria_repository.listar_categorias(db, limite)