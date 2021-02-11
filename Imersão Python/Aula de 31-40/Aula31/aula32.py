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

#-- listar todas as pessoas
def listar_todos(c):
    cursor.execute('SELECT * FROM pessoa')
    pessoas = cursor.fetchall()
    for p in pessoas:
        print(p)
# listar_todos(cursor)


#-- buscar pessoa por id
def buscar_por_id(c,id):
    c.execute(f'SELECT * FROM pessoa WHERE ID = {id}')
    pessoa = c.fetchone()
    print(pessoa)
# buscar_por_id(cursor, 2  )



#-- buscar pessoa por sobrenome
def buscar_por_sobrenome(c,sobrenome):
    c.execute(f"SELECT * FROM pessoa WHERE SOBRENOME like '%SOBRE%'")   #like == filtro... 
    for i in c.fetchall():
        print(i)
# buscar_por_sobrenome(cursor,'SOBRENOME')  # SOB retorna tudo & %SOB% retorna exatamente o que foi escrito entre %%


#-- salvar pessoa
def salvar(cn,cr,nome,sobrenome,idade,endereco_id='NULL'): #cn == conexao & cr == cursor
    cr.execute(f"INSERT INTO pessoa (NOME, SOBRENOME,IDADE,ENDERECO_ID)VALUES('{nome}', '{sobrenome}', {idade}, '{endereco_id}')")
    cn.commit()



#-- alterar pessoa
def alterar(cn,cr,id,nome,sobrenome,idade,endereco_id='Null'):
    try:
        cr.execute(f"UPDATE pessoa SET NOME='{nome}', SOBRENOME='{sobrenome}', IDADE={idade}, ENDERECO_ID={endereco_id} WHERE ID={id}")
        cn.commit()
    except(MySQLdb.Error, MySQLdb.Warning) as e:
        if(e.args[0]==1452):
            print(f"Erro de foreign Key, jovem. ID ERRADO")
        


# -- deletar pessoa
def deletar(cn, cr, id):
    cr.execute(f'DELETE FROM pessoa WHERE ID={id}')
    cn.commit()


# listar_todos(cursor)
# buscar_por_id(cursor, 3)
# buscar_por_sobrenome(cursor,'Gru')
# salvar(conexao, cursor, 'Voltolini', 'KingOfFlask', 16,5)
alterar(conexao, cursor, 8, 'Gugu Voltolini', 'KingOfBasquete', 17, 5)
# deletar(conexao, cursor, 7)