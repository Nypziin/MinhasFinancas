from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class MesesEnum(str, Enum):
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

class FaturaModel(BaseModel):
    nome_fatura: str
    mes = str
    ano = int

class FaturaCreate(FaturaModel):
    pass

class FaturaResponse(FaturaModel):
    id: int
    criada_em: datetime

    class Config:
        orm_mode = True