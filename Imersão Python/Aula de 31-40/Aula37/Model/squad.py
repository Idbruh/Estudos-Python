import MySQLdb
import sys
sys.path.append('/Users/900133/Documents/GitHub/TrabalhosPyhton/Aula37')

class Squad:
    def __init__(self):
        self.id = ''
        self.nome = ''
        self.descricao= ''
        self.numeropessoas = ''
        self.linguagembackend = ''
        self.frameworkfrontend = ''

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.numeropessoas};{self.linguagembackend};{self.frameworkfrontend}'



if __name__ == "__main__":
    squad = Squad()

