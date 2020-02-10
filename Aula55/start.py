from flask import Flask
from flask_restful import  Api

from controller import AutorController

app = Flask(__name__)
api = Api(app)

api.add_resource(AutorController, )





'''from dao.editora_dao import EditoraDao
from model.editora import Editora
from dao.base_dao import BaseDao
from model.genero import Genero

e = Editora()
editora.nome ="Novatec"

dao = EditoraDao()
dao.insert(e)

for m in dao.list_all():
    print(m.nome)

g = Genero()
g.nome = "Ficção"
g.descricao = "Só pra doido"

dao = GeneroDao()
dao.insert(g)'''