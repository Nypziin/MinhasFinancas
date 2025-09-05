from sqlalchemy.orm import Session
from app.models.categoria import Categoria
from app.schemas.categoria_schema import CategoriaCreate


def criar_categorias(db: Session, categoria: CategoriaCreate) -> Categoria:
    db_categoria = Categoria(
        nome_categoria=categoria.nome_categoria
    )
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def listar_categorias(db: Session, limite: int = 100):
    return db.query(Categoria).limit(limite).all()

def categoria_por_id(db: Session, categoria_nome: str):
    return db.query(Categoria).filter(Categoria.nome_categoria == categoria_nome).first()