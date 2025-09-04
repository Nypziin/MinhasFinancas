from sqlalchemy.orm import Session
from app.schemas.categoria_schema import CategoriaCreate
from app.repositories import categoria_repository
from app.models.categoria import Categoria
from typing import List

def criar_categoria(db: Session, categoria: CategoriaCreate) -> Categoria:
    return categoria_repository.criar_categorias(db, categoria)

def listar_gastos(db: Session, limite: int = 100) -> List[Categoria]:
    return categoria_repository.listar_categorias(db, limite)