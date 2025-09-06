from sqlalchemy.orm import Session
from app.models.fatura import Fatura
from app.schemas.fatura_schema import FaturaCreate

def criar_fatura(db: Session, fatura: FaturaCreate) -> Fatura:
    db_fatura = Fatura(
        nome_fatura=fatura.nome_fatura,
        mes=fatura.mes,
        ano=fatura.ano
    )
    db.add(db_fatura)
    db.commit()
    db.refresh(db_fatura)
    return db_fatura

def listar_faturas(db: Session, limite: int = 100):
    return db.query(Fatura).limit(limite).all()

def buscar_fatura_id(db: Session, fatura_id: int):
    return db.query(Fatura).filter(Fatura.id == fatura_id).first()