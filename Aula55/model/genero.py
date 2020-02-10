import sqlalchemy as db
from sqlalchemy import Column, Integer, String

from model.base import Base


class Genero(Base):
    __tablename__ = "LIVRARIA_GENERO"
    id = Column(Integer, primary_key=True)
    nome = String(length=100)
    descricao = String(length=250)