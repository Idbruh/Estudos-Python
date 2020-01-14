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
    cursor.execute('SELECT * FROM endereco')
    enderecos = cursor.fetchall()
    for p in enderecos:
        print(p)
# listar_todos(cursor)


#-- buscar pessoa por id
def buscar_por_id(c,id):
    c.execute(f'SELECT * FROM endereco WHERE ID = {id}')
    endereco = c.fetchone()
    print(endereco)
# buscar_por_id(cursor, 2  )




#-- buscar pessoa por sobrenome
def buscar_por_endereco(c,endereco):
    c.execute(f"SELECT * FROM endereco WHERE CIDADE like '%CID%'")   #like == filtro... 
    for i in c.fetchall():
        print(i)
# buscar_por_sobrenome(cursor,'SOBRENOME')  # SOB retorna tudo & %SOB% retorna exatamente o que foi escrito entre %%


#-- salvar pessoa
def salvar(cn,cr,logradouro,numero,complemento,bairro,cidade,cep): #cn == conexao & cr == cursor
    cr.execute(f"INSERT INTO endereco (LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO, CIDADE, CEP)VALUES('{logradouro}', '{numero}', '{complemento}', '{bairro}', '{cidade}', '{cep}')")
    cn.commit()
 



#-- alterar endereço
def alterar(cn,cr,id,logradouro,numero,complemento,bairro,cidade,cep):
    cr.execute(f"UPDATE endereco SET LOGRADOURO='{logradouro}', NUMERO='{numero}', COMPLEMENTO='{complemento}', BAIRRO='{bairro}', CIDADE='{cidade}', CEP='{cep}' WHERE ID={id}")
    cn.commit()




# -- deletar endereco
def deletar(cn, cr, id):
    cr.execute(f'DELETE FROM endereco WHERE ID={id}')
    cn.commit()


#listar_todos(cursor)
# buscar_por_id(cursor, 1)
# buscar_por_endereco(cursor,'CID')
# salvar(conexao, cursor, 'rua2', '1337','casa','bairro2','cidade2',222000)
# alterar(conexao, cursor,2,'RUA3','1337','AP 3','BAAAIRRO','CIDAADEE','2052500')
deletar(conexao, cursor, 3)