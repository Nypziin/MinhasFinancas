import enum
from datetime import datetime
from sqlalchemy import Column, Integer, Enum, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.core.database import Base


class MesesEnum(str, enum.Enum):
    janeiro = 'Janeiro'
    fevereiro = 'Fevereiro'
    marco = 'Marco'
    abril = 'Abril'
    maio = 'Maio'
    junho = 'Junho'
    julho = 'Julho'
    agosto = 'Agosto'
    setembro = 'Setembro'
    outubro = 'Outubro'
    novembro = 'Novembro'
    dezembro = 'Dezembro'


class Fatura(Base):
    __tablename__ = "faturas"
    id = Column(Integer, primary_key=True, index=True)
    nome_fatura = Column(String, nullable=False)
    mes = Column(Enum(MesesEnum, native_enum=False), nullable=False)
    ano = Column(Integer, nullable=False)
    criada_em = Column(DateTime, default=datetime.now)

    gastos = relationship("Gasto", back_populates="fatura")
