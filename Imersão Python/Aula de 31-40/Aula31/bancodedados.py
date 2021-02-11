from flask_mariadb import MariaDB
from contextlib import closing

__dados = {'host': "mysql.topskills.study",
          'database':'topskills01',
          'user':'topskills01',
          'passwd': 'ts2019',
          'port' : 3306}


def cadastrar(nome,idade):
    with closing(MySQL.db.connect(**__dados)) as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO topskills01.Bruna (nome,idade) VALUES ('{nome}','{idade};)")
        conn.commit()

def consultarAll():
    with closing(MySQL.db.connect(**__dados)) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Bruna')
        print('\nSó uma linha: ',cursor.fetchone())
        print('\nVarias linhas: ', cursor.fetchall())
    
for i in range(3):
    nome = input('digite nome: ')
    idade = int(input('digite idade: '))
    cadastrar(nome,idade)

consultarAll()



