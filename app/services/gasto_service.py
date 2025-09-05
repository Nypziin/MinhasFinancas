from sqlalchemy.orm import Session
from app.schemas.gasto_schema import GastoToPersist
from app.repositories import gasto_repository
from app.models.gasto import Gasto
from typing import List, Optional
from decimal import Decimal, ROUND_DOWN

def criar_gasto(db: Session, gasto: GastoToPersist) -> Gasto:

    valor_parcela = Decimal(gasto.valor_total) / Decimal(gasto.parcelas)
    gasto_persist = GastoToPersist(**gasto.dict(), valor_parcela=valor_parcela.quantize(Decimal("0.01"), rounding=ROUND_DOWN))

    return gasto_repository.criar_gasto(db, gasto_persist)

def listar_gastos(db: Session, limite: int = 100) -> List[Gasto]:
    return gasto_repository.listar_gastos(db, limite)

def buscar_gasto_por_id(db: Session, gasto_id: int) -> Optional[Gasto]:
    return gasto_repository.buscar_por_id(db, gasto_id)
