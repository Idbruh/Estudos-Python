import sqlalchemy as db
from sqlalchemy.orm import  relationship

from model.base import Base
from model.pessoa import Pessoa

class Autor(Pessoa):
    __tablename__ = "LIVRARIA_AUTOR"
    pseudonimo = db.Column(db.String(length=100))
    descricao = db.Column(db.String(length=100))
    pessoa_id = db.ForeignKey(db.Integer, db.ForeignKey('LIVRARIA_PESSOA.ID'))
    #pessoa = relationship(Pessoa)