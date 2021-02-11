from Model.endereco import Endereco
class Pessoa:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.sobrenome= ''
        self.idade = 0
        self.endereco = Endereco()

    def __str__(self):
        return f'{self.id};{self.nome};{self.sobrenome};{self.idade};{self.endereco}'

pessoa = Pessoa()