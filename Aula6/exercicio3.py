#-- E X E R C I C I O   1-  foreach
#Escreva programa que leia as notas (4) de 10 alunos
#armazene as notas e os nomes em listas
#imprima:
#       1- o nome dos alunos
#       2 media do aluno
#       3 -resultado (aprovado>=7.0)

nomes = []
notas = []
media = 0

a = 0
b = 1
c = 2
d = 3

for i in range(0,2): #
    nomes.append(input(f'Digite o nome do aluno {i+1}: '))
    for j in range(0,4):
        notas.append(float(input(f'Digite a nota {j+1}: ')))

for alunos in nomes:
    média = (notas [a]+notas[b]+notas[c]+notas[d])/4
    print(f'\nNome: {alunos}')
    print(f'Media: {media}')
    if media >=7:
        print('Aprovado')
    else:
        print('Reprovado')
    
    a = a+4
    b = b+4
    c = c+4
    d = c+4
##------------------jeito abioluz **** pegar do matheus s
nomes = []
notas = []

    for i in range(10):
        aluno = input(f'Digite o nome do aluno {i}: ')
        nome.append(aluno)
        listaVazia = []
        for j in range(4):
            notaAluno = float(input(f'Digite a nota {j} do aluno {aluno}: '))
            listaVazia.append(notaAluno)
        nota.append(lista_vazia)
        for k in lista_vazia:
            k = k + media
            media = 0
        for k in listaVazia:



#---------jeito Maykon
n1 = 0
n2 = 1
n3 = 2
n4 = 3

lista_alunos = []
lista_notas = []

for i in range(0,10):
    lista_alunos.append(input(f'Digite o nome do aluno {i+1}: '))
    for n in range(0,4):
        lista_notas.append(float(input(f'Digite a nota {n+1}: ')))
for aluno in lista_alunos:
    media = (lista_notas[n1] + lista_notas[n2] + lista_notas[n3 + lista_notas[n4]]) /4

    resultado = 'reprovado'
    if media >=7:
        resultado = 'Aprovado'
    print(f'Aluno: {aluno} - Média: {media} - Resultado: {resultado}')
n1 = a+4
n2 = b+4
n3 = c+4
n4 = c+4

#--------- pegar Talissa
