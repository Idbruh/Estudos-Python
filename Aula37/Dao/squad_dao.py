import MySQLdb
import sys
sys.path.append('/Users/900133/Documents/GitHub/TrabalhosPyhton/Aula37')
from Model.squad import Squad

class SquadDao:
    conexao = MySQLdb.connect(host= "127.0.0.1", database='squad', user='root', passwd= '')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = "SELECT * FROM squad.squad"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self,ID):
        comando = f"SELECT * squad WHERE ID = {ID}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squad:Squad):
        comando = f""" INSERT INTO squad
        (
            Nome,
            Descricao,
            NumeroPessoas,
            LinguagemBackEnd,
            FrameworkFrontEnd
        )
        VALUES
        (
            '{squad.nome}',
            '{squad.descricao}',
            '{squad.numeropessoas}',
            '{squad.linguagembackend}',
            '{squad.frameworkfrontend}'

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, squad:Squad):
        comando = f""" UPDATE squad
        SET
            NOME = '{squad.nome}',
            Descricao ='{squad.descricao}',
            NumeroPessoas = '{squad.numeropessoas}',
            LinguagemBackEnd = '{squad.linguagembackend}',
            FrameworkFrontEnd = '{squad.frameworkfrontend}'
        WHERE ID = {squad.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, ID):
        comando = f"DELETE FROM squad WHERE ID = {ID}"
        self.cursor.execute(comando)
        self.conexao.commit()

       