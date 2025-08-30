from sqlalchemy.orm import Session
from app.models.gasto import Gasto
from app.schemas.gasto_schema import GastoCreate
from datetime import datetime

def criar_gasto(db: Session, gasto: GastoCreate) -> Gasto:
    db_gasto = Gasto(
        nome=gasto.nome,
        categoria=gasto.categoria,
        valor_total=gasto.valor_total,
        parcelas=gasto.parcelas,
        valor_parcela=gasto.valor_parcela,
        forma_pagamento=gasto.forma_pagamento,
        tipo_gasto=gasto.tipo_gasto,
        data_compra=gasto.data_compra,
        criado_em=datetime.now()
    )
    db.add(db_gasto)
    db.commit()
    db.refresh(db_gasto)
    return db_gasto

def listar_gastos(db: Session, limite: int = 100):
    return db.query(Gasto).order_by(Gasto.data_compra.desc()).limit(limite).all()

def buscar_por_id(db: Session, gasto_id: int):
    return db.query(Gasto).filter(Gasto.id == gasto_id).first()
