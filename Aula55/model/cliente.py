import sqlalchemy as db
from sqlalchemy.orm import  relationship

from model.pessoa import Pessoa


class Cliente(Pessoa):
    __tablename__ = "LIVRARIA_CLIENTE"
    endereco = db.Column(db.String(length=100))
    numero_documento = db.Column(db.String(length=50))
    telefone = db.Column(db.String(length=20))
    pessoa_id = db.ForeignKey(db.Integer, db.ForeignKey('LIVRARIA_CLIENTE.ID'))
    pessoa = relationship(Cliente)