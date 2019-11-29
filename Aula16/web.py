from flask import Flask, render_template

app = Flask(__name__)

#meotodo retorna de uma rota
@app.route('/lista')
def listar_faixas():
    return render_template('lista.html', nome = 'lista de faixas', lista=ler_)


app.run()



#importa flask
# cria metodo
# cria no mesmo nivel de web.py a pasta "templates" e dentro da pasta cria o arquivo lista.html
# impirta metodo ler faixa -- passando com paramentro lerfaixa()
# no template {% %}  - for + nome da variavel - in - lista(metodo   finalizar {%endfor%})
# span {{ }} para imprimir usa '-' para sepaarar  e para pular linha {{\span}}<br>
# 
# 
#  