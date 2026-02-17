from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha_hash = Column(String, nullable=False)

    gastos = relationship("Gasto", back_populates="usuario")


class Gasto(Base):
    __tablename__ = "gastos"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date)
    categoria = Column(String)
    valor = Column(Float)
    tipo_pagamento = Column(String)
    descricao = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    usuario = relationship("User", back_populates="gastos")