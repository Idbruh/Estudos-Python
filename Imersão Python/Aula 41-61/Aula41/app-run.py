import sys
sys.path.append('/Users/900133/Documents/GitHub/TrabalhosPyhton/Aula41')
from flask import Flask
from flask_restful import Api


from Controllers.pessoa_controller import PessoaController


app = Flask(__name__)
api = Api(app)
api.add_resource(PessoaController, '/api/pessoa', endpoint='pessoas')
api.add_resource(PessoaController, '/api/pessoa/<int:id>', endpoint='pessoa')




@app.route('/')

def inicio():
    return '.P A G I N A.   .I N I C I A L.'

app.run(debug=True)