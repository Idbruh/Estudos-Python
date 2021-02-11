class Endereco:
    def __init__(self):
        self.id = 0
        self.logradouro = ''
        self.numero = ''
        self.complemento = ''
        self.bairro = ''
        self.cidade = ''
        self.cep = ''

    def __str__(self):
        return f'{self.id};{self.logradouro};{self.numero};{self.complemento};{self.bairro};{self.cidade};{self.cep}'