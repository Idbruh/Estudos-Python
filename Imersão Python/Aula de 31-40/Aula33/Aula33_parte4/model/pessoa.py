import MySQLdb


class Pessoa:  # primeira letra sempre maiuscula
    id = 0  # assim como dicionario, iniciar sempre com valores padroes. Abaixo está a definiçao da classe Pessoa
    nome = ''
    sobrenome = ''
    idade = 0
    enereco_id = 0
    
    def exportar_txt(self,lista_pessoas):
        with open('pessoas10.txt','a') as arquivo: 
            for p in lista_pessoas:
                arquivo.write(f"{p.id};{p.nome};{p.sobrenome};{p.idade};{p.endereco_id};\n")
    

    def __str__(self):
        return f"{self.id};{self.nome};{self.sobrenome};{self.idade};{self.endereco_ID}"