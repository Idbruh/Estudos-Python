#--- Aula 10 -  Web 3 -- calculadora
nome_pagina= 'Calculadora'
from flask import Flask, render_template, request
from calculos import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', titulo = nome_pagina)

@app.route('/calcular')
def calcular():
    n1 = int(request.args['numero1'])
    n2 = int(request.args['numero2'])
    r_soma = soma(n1,n2)
    r_subtracao = subt(n1,n2)
    r_multiplicacao = mult(n1,n2)
    r_divisao_inteira = divisao_inteira(n1,n2)
    r_divisao_fracionada = divisao_fracionada(n1,n2)
    r_resto = resto(n1,n2)
    r_raiz = raiz(n1,n2)
    resultados = {'soma':r_soma,'subtracao:':r_subtracao,'multiplicacao':r_multiplicacao,'divisao_inteira':r_divisao_inteira,'divisao_fracionada':r_divisao_fracionada,'resto': r_resto,'raiz':r_raiz}

    
    return render_template('resultado.html'
    , n1= n1
    , n2= n2
    , resultados = resultados
    )

app.run()
#-- app.run(host='endereço ip')





# return render_template('resultado.html'
#     , n1= n1
#     , n2= n2
#     , r_soma = r_soma
#     , r_subtracao = r_subtracao
#     , r_multiplicacao = r_multiplicacao
#     , r_divisao_inteira = r_divisao_inteira
#     , r_divisao_fracionada = r_divisao_fracionada
#     , r_resto = r_resto
#     , r_raiz = r_raiz