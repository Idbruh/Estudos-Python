from flask import Flask, render_template
import sys
sys.path.append('/Users/900133/Documents/GitHub/TrabalhosPyhton/Aula33/Aula33_parte4')
from controller.pessoa_controller import PessoaController
from controller.endereco_controller import EnderecoController

app = Flask(__name__)
pc = PessoaController()
ec = EnderecoController()

@app.route('/')
def inicio():
    pessoas = pc.listar_todos()
    enderecos = ec.listar_todos()
    return render_template('index.html', lista = pessoas, lista2 = enderecos)

app.run(debug=1)

    #    <style>
    #             body {
    #                 -webkit-animation: colorchange 60s infinite; 
    #                 animation: colorchange 60s infinite;
    #             }
    #             @-webkit-keyframes colorchange {
    #                  0%  {background: #33FFF3;}
    #                 25%  {background: #78281F;}
    #                 50%  {background: #117A65;}
    #                 75%  {background: #DC7633;}
    #                 100% {background: #9B59B6;}
    #             }
    #             @keyframes colorchange {
    #                  0%  {background: #33FFF3;}
    #                 25%  {background: #78281F;}
    #                 50%  {background: #117A65;}
    #                 75%  {background: #DC7633;}
    #                 100% {background: #9B59B6;}
    #             }   
    #             </style>