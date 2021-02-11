
# Aula 22 - 10-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)
# 5) Crie um metodo salvar que pegue os seguintes dados do cliente e salve em um arquivo. 
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# 6) crie um metodo que possa atualizar os dados do cliente (código cliente (inteiro), 
# nome, idade (inteiro), sexo, email, telefone). Este metodo deverá alterar tambem o dado bruto para
# que na hora de salvar o dado num arquivo, o mesmo não estaja desatualizado.

class Cliente:
    ''' esta classe recebe os dados brutos'''


    def __init__(self,dadobruto):
    
        self.dado_bruto = dadobruto
        self.codigo = None
        self.nome = None
        self.idade = None
        self.sexo= None
        self.email = None
        self.telefone = None
        self.cliente()

    def cliente(self):
        a = self.dado_bruto.split(';')
        self.codigo = int(a[0])
        self.nome = a[1]
        self.idade = a[2]
        self.sexo = a[3]
        self.email = a[4]
        self.telefone = a[5]
    
    def salvar(self,nome,atributo='a'):
        arquivo = open('Aula23/exerc_2.txt',atributo)
        arquivo.write(f'Codigo: {self.codigo}\nNome: {self.nome}\nIdade: {self.idade} anos\nSexo: {self.sexo}\nEmail: {self.email}\nTelefone: {c.telefone}')
        arquivo.close()   

        #-- ou
        def salvar(self,nome,atributo='a'):
            if atributo == 'a':
                arquivo = open('Aula23/exerc_2.txt',atributo)
                arquivo.write(f'Codigo: {self.codigo}\nNome: {self.nome}\nIdade: {self.idade} anos\nSexo: {self.sexo}\nEmail: {self.email}\nTelefone: {c.telefone}')
                arquivo.close()   

    
    def atualizar(self,codigo,nome,idade,sexo,email,telefone):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.email = email
        self.telefone = telefone
        self.dado_bruto = f'Codigo: {self.codigo}\nNome: {self.nome}\nIdade: {self.idade} anos\nSexo: {self.sexo}\nEmail: {self.email}\nTelefone: {self.telefone}'
        self.salvar('arquivo')
        
            
   
c = Cliente(dadobruto)
c.salvar()
c.cliente()
c.atualizar(1,'Bruna',27,'f','b@b.com','41998683867')
print(c.nome)

