import sys
sys.path.append('/Users/900133/Documents/GitHub/TrabalhosPyhton/Aula41')
import MySQLdb


from Model.endereco_model import _model import EnderecoModel


class EnderecoDao:
    def __init__(self):
        self.connection = MySQLdb.connect(host= "127.0.0.1", database='squad', user='root', passwd= '')
        self.cursor = self.connection.cursor()


    def list_all(self):
        self.cursor.execute("SELECT * FROM `bruna-aula31-db`.endeeco")
        enderecos = self.cursor.fetchall()
        lista_endreco = []
        for e in enderecos:
            endereco = EnderecoModel(e[1],e[2],e[3],e[0])
            lista_pessoa.append(pessoa.__dict__)

        return lista_pessoa

    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM `bruna-aula31-db`.pessoa WHERE ID = {}".format(id))
        pessoa = self.cursor.fetchone()
        p = PessoaModel(pessoa[1], pessoa[2], pessoa[3], pessoa[0])
        return p.__dict__

    def insert(self, pessoa:PessoaModel):
        self.cursor.execute("INSERT INTO `bruna-aula31-db`.pessoa (NOME, SOBRENOME, IDADE) VALUES('{}','{}',{})".format(pessoa.nome, pessoa.sobrenome, pessoa.idade))
        self.connection.commit()
        id = self.cursor.lastrowid
        pessoa.id = id
        return pessoa.__dict__

    def update(self, pessoa:PessoaModel):
        self.cursor.execute("UPDATE `bruna-aula31-db`.pessoa SET NOME = '{}', SOBRENOME = '{}', IDADE = {} WHERE ID = {}".format(pessoa.nome, pessoa.sobrenome, pessoa.idade, pessoa.id))
        self.connection.commit()
        return pessoa.__dict__

    def remove(self,id):
        self.cursor.execute("DELETE FROM `bruna-aula31-db`.pessoa WHERE ID = {}".format(id))
        self.connection.commit()
        return 'Removido a pessoa de id: {}'.format(id)


    #model - dao - controller