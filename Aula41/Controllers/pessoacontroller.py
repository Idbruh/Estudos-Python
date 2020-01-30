from flask_restful import Resource

class PessoaController(Resource):
    def get(self):
        return 'Metodo: GET -- Quando chamamos retorne uma string.'

    def post(self):
        return 'Metodo: POST -- Quando chamamos retorne uma string.'

    def put(self):
        return 'Metodo: PUT -- Quando chamamos retorne uma string.'

    def delete(self):
        return 'Metodo: DELETE -- Quando chamamos retorne uma string.'