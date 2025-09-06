from typing import List, Optional
from app.models.fatura import Fatura
from app.schemas.fatura_schema import FaturaCreate
from app.repositories import fatura_repository
from sqlalchemy.orm import Session


def criar_fatura(db: Session, fatura: FaturaCreate) -> Fatura:
    return fatura_repository.criar_fatura(db, fatura)

def listar_faturas(db: Session, limite: int = 100) -> List[Fatura]:
    return fatura_repository.listar_faturas(db, limite)

def listas_fatura_id(db: Session, fatura_id: int) -> Optional[Fatura]:
    return fatura_repository.buscar_fatura_id(db, fatura_id)

