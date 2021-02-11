# Aula 21 - 16-12-2019
#Funções para listas

from geradorlista import lista_simples_int
from random import randint

lista1 = lista_simples_int(randint(5,100))
lista2 = lista_simples_int(randint(5,75))
lista3 = lista_simples_int(randint(5,70))


print('1) Com as listas aleatórias (lista1,lista2,lista3) e usando as funções para listas, # f-string, responda as seguintes questões:')
# f-string, responda as seguintes questões:


# 1.1) Qual é o tamanho da lista1?
print(f'O tamanho da lista 1 é: {len(lista1)}')


# 1.2) Qual é o maior valor da lista2?
print(f'O maior valor da lista2 {max (lista2)}')


# 1.3) Qual seria a soma do maior valor com o menor valor da lista2?
print(f'A soma do maior valor com o menor valor da lista2 é: {max(lista2)+min(lista2)}')

# 1.4) Qual é a média aritmética da lista1?
print(f'A media entre os numeros da lista1 é: {(sum(lista1)) / (len(lista1))}')

# 1.5) Qual o valor da soma de todas as listas e a soma total delas?
# quero que mostre a soma individual (por lista) e a soma total de todas elas (soma das somas das listas)
so1 = (sum(lista1))
so2 = (sum(lista2))
so3 = (sum(lista3))
soma = (so1 + so2 + so3)
print(f'A soma da lista1 é {so1}')
print(f'A soma da lista2 é {so2}')
print(f'A soma da lista3 é {so3}')
print(f'A soma de todas as listas é: {soma}')


# 1.6) Usando o f-string, imprima todos os valores da lista1 um de baixo do outro.
a = ('---'*30)
print(a)
print('todos os valores da lista1 um de baixo do outro:')
for i in lista1:
    print(f'{i}')
print(a)


# 1.7) Com a indexação e f-string, mostre o valor das posições 5, 9, 10 e 25 de cada lista.
# trate para evitar o erro: IndexError


print(a)
try:
    print(f'Lista 1: posição 5: {lista1[5]} - posição 9:  {lista1[9]} - posição 10: {lista1[10]} - posição 25: {lista1[25]}')
except IndexError:
    print('errrou')
try:
    print(f'Lista 2: posição 5: {lista2[5]} - posição 9: {lista2[9]} - posição 10: {lista2[10]} - posição 25:  {lista2[25]}')
except IndexError:
    print('errrou')
try:
    print(f'Lista 3: posição 5: {lista3[5]} - posição 9:  {lista3[9]} - posição 10: {lista3[10]} - posição 25:  {lista3[25]}')
except IndexError:
    print('errrou')
print(a)
# 1.8) Mostre qual das listas tem mais itens (lembre-se, as listas são randômicas, não há como prever o 
# tamanho delas).
print(a)
lista1 < lista2
if lista2 < lista3:
    print('Lista 2 é a maior')
elif lista3 < lista1:
    print('Lista 3 é a maior')
else:
    print('Lista 1 é a maior')
print(a)

# 1.9) Some os maiores números de todas as listas e subtraia pelo menor número dos menores valores das listas.
# Para obter o menor valor, pegue o menor valor das listas e veja qual deles é o menor e use ele.
aaa = (max(lista1) + max(lista2) + max(lista3))
bbb = (min(lista1) + min(lista2) + min(lista3))
dife = aaa - bbb
print(dife)


# 1.10) Pegue o maior valor de todas as listas e some com o menor valor de todas as listas







