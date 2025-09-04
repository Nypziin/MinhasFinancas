from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.gasto import FormaPagamentoEnum, TipoGastoEnum

router = APIRouter(prefix="/enum", tags=["Enums"])

@router.get("/formas-pagamento")
def listar_formas_pagamento():
    return [{"key": f.name, "value": f.value} for f in FormaPagamentoEnum]

@router.get("/tipos-gasto")
def listar_tipo_gasto():
    return [{"key": f.name, "value": f.value} for f in TipoGastoEnum]