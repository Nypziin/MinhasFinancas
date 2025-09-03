from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.gasto import FormaPagamentoEnum

router = APIRouter(prefix="/enum", tags=["FormasPagamento"])

@router.get("/formas-pagamento")
def listar_formas_pagamento():
    return [{"key": f.name, "value": f.value} for f in FormaPagamentoEnum]

