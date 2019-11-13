#-- E X E R C I C I O   1-  foreach
#Escreva programa que leia as notas (4) de 10 alunos
#armazene as notas e os nomes em listas
#imprima:
#       1- o nome dos alunos
#       2 media do aluno
#       3 -resultado (aprovado>=7.0)


lista_alunos = []
lista_notas = []

lista_alunos = []

for i in range(1,10):
    nome = input(f'Nome dos alunos {i}: ')
    lista_alunos.append(nome)
print(lista_alunos)
