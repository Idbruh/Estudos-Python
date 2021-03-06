import sys
sys.path.append('/Users/900133/Documents/GitHub/TrabalhosPyhton/Aula41')
from flask_restful import Resource
from flask import request


from Dao.pessoa_dao import PessoaDao
from Model.pessoa_model import PessoaModel


class PessoaController(Resource):

    def __init__(self):
        self.dao = PessoaDao()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()

    def post(self):
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        idade = int(request.json['idade'])
        pessoa = PessoaModel(nome, sobrenome, idade)
        msg = self.dao.insert(pessoa)
        return msg

    def put(self, id):
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        idade = int(request.json['idade'])
        pessoa = PessoaModel(nome, sobrenome, idade, id)
        msg = self.dao.update(pessoa)
        return msg

    def delete(self, id):
        return self.dao.remove(id)