from sqlalchemy import Column, Integer, String, DateTime, Date, Numeric, Enum
from sqlalchemy.ext.declarative import declarative_base
from app.core.database import Base


class Categoria(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True, index=True)
    nome_categoria = Column(String, nullable=False)
