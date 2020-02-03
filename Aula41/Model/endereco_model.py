import sys
sys.path.append('/Users/900133/Documents/GitHub/TrabalhosPyhton/Aula41')

class EnderecoModel:
    def __init__(self,logradouro,numero,complemento,bairro,cidade,cep,id=0):
        self.id = id
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep