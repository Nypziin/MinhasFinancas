from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.gasto_schema import GastoCreate, GastoResponse
from app.services import gasto_service
from app.core.database import SessionLocal

router = APIRouter(prefix="/gastos", tags=["Gastos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=GastoResponse)
def criar_gasto(gasto: GastoCreate, db: Session = Depends(get_db)):
    return gasto_service.criar_gasto(db, gasto)

@router.get("/", response_model=List[GastoResponse])
def listar_gastos(db: Session = Depends(get_db), limite: int=100):
    return gasto_service.listar_gastos(db, limite)

@router.get("/{gasto_id}", response_model=GastoResponse)
def buscar_por_id(gasto_id: int, db: Session = Depends(get_db)):
    gasto = gasto_service.buscar_gasto_por_id(db, gasto_id)
    if not gasto:
        raise HTTPException(status_code=404, detail="Gasto não encontrado")
    return gasto


