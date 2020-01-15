import MySQLdb

class Pessoa:  # primeira letra sempre maiuscula
    id = 0  # assim como dicionario, iniciar sempre com valores padroes. Abaixo está a definiçao da classe Pessoa
    nome = ''
    sobrenome = ''
    idade = 0
    enereco_id = 0
    
    def exportar_txt(self,lista_pessoas):
        with open('Aula33_parte4/pessoas.txt','a') as arquivo: 
            for p in lista_pessoas:
                arquivo.write(f"{p.id};{p.nome};{p.sobrenome};{p.idade};{p.endereco_id};\n")


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




    def __str__(self):
        return f"{self.id};{self.nome};{self.sobrenome};{self.idade};{self.endereco_ID}"