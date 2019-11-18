# AULA 8  - W E B

from flask import Flask

app = Flask(__name__)
@app.route('/')
def inicio():
    return 'Bem vindos ao mundo real, meus queridos'

app.run()