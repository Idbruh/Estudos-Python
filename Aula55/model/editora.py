import sqlalchemy as db

from model.base import Base


class Editora:
    __tablename__ = "LIVRARIA_EDITORA"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))
