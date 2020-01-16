import MySQLdb
from model.endereco import Endereco


class EnderecoaDb:
    conexao = MySQLdb.connect(host= "127.0.0.1", database='bruna-aula31-db', user='root', passwd= '')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando_sql_select = "SELECT * FROM endereco"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchall() 
        return self.converter_tabela_dicionario_classe
    
    def buscar_por_id(self,id):
        comando_sql_select = "SELECT * FROM endereco"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchone() 
        return resultado

    def converter_tabela_dicionario_classe(lista_tuplas):

        lista_enderecos = []
        for p in lista_tuplas:
            e1 = Endereco()
            print(e[0],e[1]) 
            e1.id = p[0]
            e1.logradouro = p[1]
            e1.numero = p[2]
            e1.complemento = p[3]
            e1.bairro = p[4]
            e1.cidade = p[5]
            e1.cep = p[6]
            lista_enderecos.append(e1) 
        return lista_enderecos

