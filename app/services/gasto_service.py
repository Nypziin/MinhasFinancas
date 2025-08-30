from sqlalchemy.orm import Session
from app.schemas.gasto_schema import GastoCreate
from app.repositories import gasto_repository
from app.models.gasto import Gasto
from typing import List, Optional

def criar_gasto(db: Session, gasto: GastoCreate) -> Gasto:
    return gasto_repository.criar_gasto(db, gasto)

def listar_gastos(db: Session, limite: int = 100) -> List[Gasto]:
    return gasto_repository.listar_gastos(db, limite)

def buscar_gasto_por_id(db: Session, gasto_id: int) -> Optional[Gasto]:
    return gasto_repository.buscar_por_id(db, gasto_id)
