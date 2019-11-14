#-- E X E R C I C I O   1-  Listas
#Escreva programa que leia o nome de 10 anlunos
#Armazene os nomes em uma lista
#imprima a lista

lista_alunos = []

'''for i in range(1,10):
    nome = input(f'Nome dos alunos {i}: ')
    lista_alunos.append(nome)
print(lista_alunos)'''

for i in range(0,10):
    lista_alunos.append(input('Nome dos alunos: '))
print(lista_alunos)
