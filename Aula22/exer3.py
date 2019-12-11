# Aula 22 - 10-12-2019
# # Como Tratar e Trabalhar Erros!!!

# Dica: O mais importante é conseguir fazer! Não importa como chegou ao resultado e sim o resultado!

# Dica2: na função .open() você pode escolher entre 'r' para ler, 'w' para sobrescrever e criar um 
# arquivo novo ou o 'a' que é abreveativo de append, onde ele inclui linha no final do arquivo.
# Você sabia que o 'r', 'w' e o 'a' são string que podem ser passadas via variável exemplo:

# atributo = 'r'
# nome_arquivo = 'cadastro'
# arquivo.open(f'exercicio/{nome_arquivo}.txt',atributo)



# 1) Crie uma classe cadastro.
# Esta classe deve abrir o arquivo cadastro2.txt e guardar os cadastro numa lista com dicionários.

# 2) crie o metodo salvar os dados dos clientes em um arquivo txt.
# 3) crie um metodo para cadastrar novos clientes. O código cliente é unico por pessoa, sendo assim não pode 
# se repetir.
# 3) Crie um metodo de consulta de cliente, mostrando os dados dele na tela.
# 4) Crie um metodo para atualizar o cadastro de um cliente qualquer pelo codigo cliente.
# Após atualizar, salvar todos no arquivo "cadastro_atualizado.txt" (use o 'w' para sobrescrever o arquivo.)
#
#  Observação: Use o try/filnaly para abrir e fechar os arquivos. Veja na aula 21- Ecessões como é!


class Pessoa:
    '''
    Esta classe recebe cadastro
    '''
    def __init__(self,codigo,nome,idade,sexo,email,telefone):
        # self.cadastro = cadastro
        # self.pessoa = pessoa
        self.codigo = codigo
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.email = email
        self.telefone = telefone
    
    def __str__(self):
        texto = f'''
    Codigo: {self.codigo}
    Nome: {self.nome}
    Idade: {self.idade}
    Sexo: {self.sexo }
    E-mail: {self.email} 
    Telefone: {self.telefone}'''

        return texto


    def __eq__(self,valor):
        return self.codigo == valor


class Cadastro:
    def __init__(self):
        self.lista = []
        self.ler_cadastro()
    
    def ler_cadastro(self):
        arquivo = open('Aula22/cadastro2.txt','r')
        for pessoa in arquivo:
            pessoa = pessoa.strip().split(';')
        # for pessoa in arquivo:
            codigo = int( pessoa[0] )
            nome = pessoa[1]
            idade = int( pessoa[2] )
            sexo = pessoa[3]
            email = pessoa[4]
            telefone = pessoa [5]

            self.lista.append(Pessoa(codigo,nome,idade,sexo,email,telefone))

    def consulta(self):
        codigo = int(input('Digite um codigo: '))
        for linha in self.lista:
            if linha == codigo:
                print(linha)
                break


a = Cadastro()
a.consulta()
    





