#-- IMPORTAR BIBLIOTECA DO MySQL
import MySQLdb

def listar_todos():
    conexao = MySQLdb.connect(host= "127.0.0.1", database='bruna-aula31-db', user='root', passwd= '')
    cursor = conexao.cursor()
    dicionario_pessoa = {'Id': 0, 'Nome': '', 'Sobrenome': '', 'Idade': 0, 'Endereco_ID': 0}
    lista_pessoas = [] 
    comando_sql_select = "SELECT * FROM pessoa"
    cursor.execute(comando_sql_select)
    resultado = cursor.fetchall() 
    return resultado