import uuid
from sqlalchemy.orm import Session
from app.schemas.gasto_schema import GastoToPersist
from app.repositories import gasto_repository
from app.models.gasto import Gasto
from typing import List, Optional
from decimal import Decimal, ROUND_HALF_UP

def criar_gasto(db: Session, gasto: GastoToPersist) -> Gasto:

    valor_parcela = (Decimal(str(gasto.valor_total)) / Decimal(gasto.parcelas)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    primeiro_gasto: Optional[Gasto] = None

    uuid_grupo = str(uuid.uuid4())

    for parcela in range(gasto.parcelas):
        gasto_persist = GastoToPersist(**gasto.dict(), valor_parcela=valor_parcela, parcela_atual=parcela+1, grupo_id=uuid_grupo)
        gasto_criado = gasto_repository.criar_gasto(db, gasto_persist)

        if primeiro_gasto is None:
            primeiro_gasto = gasto_criado

    return primeiro_gasto

def listar_gastos(db: Session, limite: int = 100) -> List[Gasto]:
    return gasto_repository.listar_gastos(db, limite)

def buscar_gasto_por_id(db: Session, gasto_id: int) -> Optional[Gasto]:
    return gasto_repository.buscar_por_id(db, gasto_id)
