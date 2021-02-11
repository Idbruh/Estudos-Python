# Aula 6 -- L I S T A S
#inicialização de uma variavel tipo lista
lista1 = []
#inicialização de uma variavel tipo lista, com elementos
lista2 = ['Marcela', 'Nicole', '*Matheus', 10] #'*exemplo' == todos os que possuem o mesmo nome
#lista inteiros
lista3 = [1,2,3,4]
#lista de tipos diferentes
lista4 = [1,"idbruh",12.5]

#impressão das lista criadas
print(lista1)
print(lista2)
print(lista3)

# ------------- adicionando elementos em uma lista já criada
# lista.(vai abrir uma lista--- ler metodos os disponiveis)
# ler erros e tentar achar a solução para o problema
lista1.append(lista2)
lista1.append(lista3)

#------------------impressão de lista vindas da função INPUT   
lista1.append(input('Digite o nome do seu artista favorito: '))


lista_perguntas1 = [input('digite artista'), input('digite endereço')]

print(lista_perguntas1)
#print lista_perguntas

posicao = int(input('Digite a posição: '))
print( lista2[posicao-1] )
