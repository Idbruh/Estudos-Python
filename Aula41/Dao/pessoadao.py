import MySQLdb

from Aula41.Model.pessoamodel import PessoaModel


class PessoaDao:
    def __init__(self):
        self.connection = MySQLdb.connect(host='mysql.topskills.dev', database='topskills01', user='topskills01', passwd='ts2019')
        self.cursor = self.connection.cursor()
        pessoas = self.cursor.fetchall()
        return pessoas

    def list_all(self):
        self.cursor.execute("SELECT * FROM `bruna-aula31-db`.pessoa")
        return 'Listando todos os dados da tabela'

    def get_by_id(self):
        self.cursor.execute(f"SELECT * FROM `bruna-aula31-db`.pessoa WHERE ID={ID}")
        return 'Listando o dado de id: {}'.format(id)

    def insert(self, pessoa):
        return 'Cadastrando uma pessoa'

    def update(self, pessoa):
        return 'Alterando uma pessoa'

    def remove(self,id):
    self.cursor.execute("DELETE FROM WHERE ID {}".format(id))
        return 'Removendo a pessoa de id: {}'.format(id)