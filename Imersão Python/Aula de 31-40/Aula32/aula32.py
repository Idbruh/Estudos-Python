#-- pip3 install flask_mysqldb 
#-- referencia ao mwsql


import MySQLdb

conexao = MySQLdb.connect(host= "127.0.0.1", database='bruna-aula31-db', user='root', passwd= '')

cursor=conexao.cursor()
# cursor.execute('SELECT * FROM pessoa')
# pessoas = cursor.fetchall()


# for p in pessoas:
#     print(p)
# # ou

def listar_todos(c):
    cursor.execute('SELECT * FROM pessoa')
    pessoas = cursor.fetchall()
    for p in pessoas:
        print(p)

# listar_todos(cursor)

def buscar_por_id(c,id):
    c.execute(f'SELECT * FROM pessoa WHERE ID = {id}')
    pessoa = c.fetchone()
    print(pessoa)

# buscar_por_id(cursor, 2  )

def buscar_por_sobrenome(c,sobrenome):
    c.execute(f'SELECT * FROM pessoa WHERE SOBRENOME like = {sobrenome}')   #like == filtro... 
    pessoa = c.fetchall()
    print(pessoa)

buscar_por_sobrenome(cursor,'SOB')  # SOB retorna tudo & %SOB% retorna exatamente o que foi escrito entre %%