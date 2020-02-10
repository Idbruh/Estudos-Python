import sqlalchemy as db
from  sqlalchemy import  relationship
from model.base import Base



class Livro(Base):
    __tablename__ = "LIVRARIA_LIVRO"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(length=100))
    sinopse = db.Column(db.String(length=100))
    data_primeira_publicacao = db.Column(db.Date)
    autor_id = db.Column(db.Integer, db.ForeignKey('LIVRARIA_AUTOR.IG'))
    autor = relationship(Autor)
    editora_id = db.Column(db.Integer, db.ForeignKey())
    editora = relationship(Editora)
    genero_id = db.Column(db.Integer, db.ForeignKey())
    genero = relationship(Genero)
