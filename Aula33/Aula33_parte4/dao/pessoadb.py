import MySQLdb
from model.pessoa import Pessoa


class PessoaDb:
    conexao = MySQLdb.connect(host= "127.0.0.1", database='bruna-aula31-db', user='root', passwd= '')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando_sql_select = "SELECT * FROM pessoa"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchall() 
        return self.converter_tabela_dicionario_classe
    
    def buscar_por_id(self,id):
        comando_sql_select = "SELECT * FROM pessoa"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchone() 
        return resultado

    def converter_tabela_dicionario_classe(lista_tuplas):

        lista_pessoas = []
        for p in lista_tuplas:
            p1 = Pessoa()
            print(p[0],p[1]) 
            p1.id = p[0]
            p1.nome = p[1]
            p1.sobrenome = p[2]
            p1.idade = p[3]
            p1.endereco_id =p[4]
            lista_pessoas.append(p1) 
        return lista_pessoas


