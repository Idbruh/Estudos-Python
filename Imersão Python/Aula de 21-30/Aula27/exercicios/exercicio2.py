# Aula 21 - 16-12-2019
#Operadores in is ==

from geradorlista import lista_simples_int_str
from geradorlista import lista_simples_int
from geradorlista import lista_simples_str
from geradorlista import embaralhar


# A função embaralhar() irá criar listas aleátorias, copiar-las
# e embaralhar. Desta forma não se sabe se as listas são iguais ou
# se as listas são as mesmas. Como defult ela irá criar 3 listas
# diferentes com 30 itens, copiálas e embaralar randomicamente
# retornando uma lista com o dobro (6) de itens.

lista = embaralhar(2,10)

a = lista[0]
b = lista[1]
c = lista[2]
d = lista[3]

# print(a)
# print(b)
# print(c)
# print(d)

# Neste caso, ele irá criar 2 listas com 10 itens, e retornará
# uma lista com 4 listas podendo cada uma ser cópia ou uma só.




# lista = embaralhar(2,10,2)

# print(lista)

# 1) Analisnado a lista gerada (possui 2 listas), diga se as duas listas são elas
# mesmas (is) ou são somente iguais (==).
if lista[0] == lista[1]:
    print('elas são iguais')
else:
    print('elas não são iguais')
if lista[0] is lista[1]:
    print('elas são as mesmas')
else:
    print('elas não são as mesmas')



# 2) Qual é o maior valor destas duas listas 
if max(lista[0]) < max(lista[1]):
    print(f'o maior numéro entre as listas é: {max(lista[0])}')
else:
    print(f'o maior numéro entre as listas é: {max(lista[1])}')

# 3) Qual é o maior valor de cada lista
print(f'{max(lista[0])} - { max(lista[1])}')

# 4) Há o número 10 dentro da lista[0]?
if lista[0].count(10) == True:
    print('Existe o numero 10 na lista[0]')
else:
    print('não existe o numero 10 na lista[0]')


# 5) Há o número 20 dentro da lista[1]?
if lista[1].count(20) == True:
    print('Existe o numero 20 na lista[0]')
else:
    print('não existe o numero 20 na lista[0]')


# 6) Quantos números da lista[0] tem dentro da lista[1]?
contador = 0
for i in lista[0]:
    if i in lista[1]:
        contador += 1
print(f'existem {contador} repetidos')


# 7) Mostre os números da lista[0] que estão dentro da lista[1]
num = []
for i in lista[0]:
    if i in lista[1]:
        num.append(str(i))
print(f'os números da lista[0] que estão dentro da lista[1] são: {" ".join(num)}')

# 8) Mutliplique a soma da lista[0] com cada item da lista[1]

for i in lista[1]:
    print(f'O resultados da multiplicação entre a soma de {sum(lista[0])} por {i} é {(sum(lista[0]))*i}')

# 9) Faça uma divisão inteira do maior número da lista pelo menor numero da lista. Após verifique 
# se o resultado está dentro de uma das listas, se sim, diga qual!
r_div0 = min(lista[0]) // max(lista[0])
r_div1 = min(lista[1]) // max(lista[1])

if r_div0 in lista:
    print(f'{r_div0} está na Lista: {lista.count(r_div0)}')
else:
    print('O resultado da divisão inteira de Lista[0] não está na lista')

if r_div1 in lista:
    print(f'{r_div1} está na Lista: {lista.count(r_div1)}')
else:
    print('O resultado da divisão inteira de Lista[1] não está na Lista')



# 10) verifique se o maior número da lista[0] está dentro da lista[1] e se o menor número da
# lista[1] está na lista[0]

if max(lista[0]) in lista[1]:
    print('O maior numero da lista[0] está dentro da lista[1]')
if min(lista[1]) in lista[0]:
    print('O menor numero da lista[1] está dentro da lista[0]')




