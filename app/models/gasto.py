from sqlalchemy import Column, Integer, String, DateTime, Date, Numeric, Enum
from sqlalchemy.ext.declarative import declarative_base
from app.core.database import Base
from datetime import datetime
import enum


class FormaPagamentoEnum(str, enum.Enum):
    credito = "Crédito"
    debito = "Débito"
    pix = "Pix"
    dinheiro = "Dinheiro"


class TipoGastoEnum(str, enum.Enum):
    fixo = "Fixo"
    variavel = "Variável"


class Gasto(Base):
    __tablename__ = "gastos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    valor_total = Column(Numeric(10, 2), nullable=False)
    parcelas = Column(Integer, default=1)
    valor_parcela = Column(Numeric(10, 2), nullable=False)
    forma_pagamento = Column(Enum(FormaPagamentoEnum, native_enum=False), nullable=False)
    tipo_gasto = Column(Enum(TipoGastoEnum, native_enum=False), nullable=False)
    data_compra = Column(Date, nullable=False)
    criado_em = Column(DateTime, default=datetime.now)

