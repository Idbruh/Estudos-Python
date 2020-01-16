class Endereco:  # primeira letra sempre maiuscula
    id = 0  # assim como dicionario, iniciar sempre com valores padroes. Abaixo está a definiçao da classe endereco
    lograduro = ''
    numero = 0
    complemento = ''
    bairro = ''
    cidade = ''
    cep = ''
    
    def exportar_txt(self,lista_enderecos):
        with open('endereco.txt','a') as arquivo: 
            for e in lista_enderecos:
                arquivo.write(f"{e.id};{e.lograduro};{e.complemento};{e.bairro};{e.cidade};{e.cep}\n")
    

    def __str__(self):
        return f"{self.id};{self.lograduro};{self.complemento};{self.bairro};{self.cidade};{self.cep}"

        
