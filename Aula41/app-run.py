from flask import Flask
from flask_restful import Api

from Controllers.pessoacontroller import PessoaController

app = Flask(__name__)
api = Api(app)
api.add_resource(PessoaController, '/api/pessoa, endpoint='pessoas')
api.add_resource(PessoaController, '/api/pessoa/<int:id>,endpoint='pessoa')

@app.route('/')

def inicio():
    return 'qualquer coisa como string'

app.run(debug=True)