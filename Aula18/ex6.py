# Aula 18 - 03-11-2019

# Festa da HBSIS

# 1 - Faça uma função que leia do arquivo cadastro.txt e
#  retorne uma lista com dicionários.
# cada linha possui os dados na seguinte posição:
#  codigo, nome, sexo, idade

# 2 - Como a entrada da festa é mais barata para mulheres (R$ 15,00) 
# do que para os homens (R$ 35,00) 
# deve-se separar os dois em duas listas separadas
#  e salvar em arquivos separados. Como é uma festa de arromba,
# menores de idade não podem entrar.

# 3 - Faça uma terceira função que ao digitar
#  o código do participante ele imprima o nome do participante, 
# o valor do ingresso, e em caso de menores de
#  idade apareça o texto "Entrada Proibida!"


arquivo = open('Aula18\cadastro_exer6.txt','r')
#conteudo = arquivo.read()

# linhas_do_arquivo = conteudo.split('\n')
# primeira_linha = linhas_do_arquivo[0]
# lista_da_primeira_linha = primeira_linha.split(';')

# a = ('--' * 50)

# print(a)
# print(primeira_linha)
# print(a)
# print(primeira_linha.split[1])


def ler_cadastro():
   arquivo = open('18-Aula18/exercicios/cadastro.txt','r')
   lista = []
   for pessoas in arquivo:
      pessoas = pessoas.strip().split(';')
      dicionario = {'codigo':pessoas[0], 'nome':pessoas[1], 
                    'sexo':pessoas[2], 'idade':pessoas[3]}
      lista.append(dicionario)
   arquivo.close()
   return lista

def lista_festa(lista_de_entradas):
   lista_homens = []
   lista_mulheres = []

   for pessoa in lista_de_entradas:
      if int(pessoa['idade']) >= 18:
         if pessoa['sexo'] == 'f':
            lista_mulheres.append(pessoa)
         else:
            lista_homens.append(pessoa)

   salvar(lista_homens,'homens')
   salvar(lista_mulheres,"mulheres")

def salvar(lista,nome):
   arquivo = open(f'18-Aula18/exercicios/{nome}.txt','a')
   for pessoa in lista:
      texto = f"{pessoa['codigo']};{pessoa['nome']};{pessoa['sexo']};{pessoa['idade']}\n"
      arquivo.write(texto)
   arquivo.close()

def consulta(lista_consulta_funcao,numero):
   for lista_consulta in lista_consulta_funcao:
      if int(lista_consulta['codigo']) == numero:

         if int(lista_consulta['idade']) >= 18:
            if lista_consulta['sexo'] == 'f':
               print(f"Nome: {lista_consulta['nome']} valor ingresso: R$ 15,00 ")
            else:
               print(f"Nome: {lista_consulta['nome']} valor ingresso: R$ 35,00 ")
         else:
            print(' Não Pode Entrar!')


lista1 = ler_cadastro()
lista_festa(lista1)

while True:
   a=int(input('Digite um numero: '))
   consulta(lista1,a)




'''registros = [] 
campos = ('codigo', 'nome','sexo','idade' ) 

for linha in arquivo:
    dados = linha.strip().split(';')
    dicionario = {}
    # dicionario = ['codigo'] = dados[0]
    # dicionario = ['nome'] = dados[1]
    # dicionario = ['sexo'] = dados[2]
    # dicionario = ['idade'] = dados[3]
    i = 0
    for campo in dados:
        dicionario[campo] = dados[i]
        i = i + 1
    registros.append(dicionario)
print(registros)

def ler_cadastro():
    arquivo = open('Aula18/cadastro_exer6.txt','r')
    lista = []
    for pessoas in arquivo:
        pessoas = pessoas.strip().split(';')
        dicionario = {'codigo':pessoas[0], 'nome':pessoas[1], 'idade':pessoas[2], 'idade':pessoas[3]}
        lista.append(dicionario)
    arquivo.close()
    return lista
print(ler_cadastro())

def lista_festa(lista_de_entradas):
    lista_mulheres = []
    lista_homens = []
    for pessoa in lista_de_entradas:
        if int(pessoa['idade']) >= 18:#converter os dados 'string' para inteiro(int)
            if pessoa['sexo'] == 'f':
                lista_mulheres.append(pessoa)
            else:
                lista_homens.append(pessoa)
        salvar(lista_homens,'homens')
        salvar(lista_mulheres,'mulheres')

def salvar(lista,nome):
    arquivo = open(f'Aula18/cadastro_exer6{nome}.txt','a')
    for pessoa in lista:
        texto = f"{pessoa['codigo']};{pessoa['nome']};{pessoa['sexo']};{pessoa['idade']}\n"
        arquivo.write(texto)
    arquivo.close()

def consulta(lista_consulta,numero):
    for lista_consulta in lista_consulta_função:
        if int(lista_consulta['codigo']) == numero:   
    if int(lista_consulta['idade']) >= 18:
        if lista_consulta['sexo'] == 'f':
            print(f"{lista_consulta['nome']} valor: R$ 15,00")
        else:
            print(f"{lista_consulta['nome']} valor: R$ 35,00")
    else:
        print('Entrada não autorizada!')

lista1 = ler_cadastro()
lista_festa(lista1)

while True:
    a = int(input('Digite um numero: '))
    consulta(lista1,a)












'''
codigo = input("digite o código: ")
nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
sexo = input('Digite 1. Feminino | 2. Marculino: ')




def'''

