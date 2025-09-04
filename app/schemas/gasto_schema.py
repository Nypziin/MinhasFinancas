from pydantic import BaseModel, Field
from datetime import date, datetime
from enum import Enum


class FormaPagamentoEnum(str, Enum):
    credito = "Crédito"
    debito = "Débito"
    pix = "Pix"
    dinheiro = "Dinheiro"

class TipoGastoEnum(str, Enum):
    fixo = "Fixo"
    variavel = "Variável"

class GastoBase(BaseModel):
    nome: str
    categoria: str
    valor_total: float = Field(..., gt=0)
    parcelas: int = 1
    valor_parcela: float = Field(..., gt=0)
    forma_pagamento: FormaPagamentoEnum
    tipo_gasto: TipoGastoEnum
    data_compra: date

class GastoCreate(GastoBase):
    pass

class GastoResponse(GastoBase):
    id: int
    criado_em: datetime

    class Config:
        orm_mode = True
