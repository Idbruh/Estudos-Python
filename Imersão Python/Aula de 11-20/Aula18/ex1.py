# Aula 18 - 03-11-2019
# Exercicios para lista simples


# Dada a seguinte lista, resolva os seguintes questões:

lista = [10, 20, 'amor', 'abacaxi', 80, 'Abioluz', 'Cachorro grande é de arrasar']
#    # = 0    1    2        3        4     5                   6

#--1 imprima o item 'abacaxi'
print(lista[3])

#--2: Usando a indexação, escreva na tela os seguintes dados: 20, amor, abacaxi'
print(lista[1:4])

#--3 Usando a indexação, escreva na tela uma lista com dados de 20 até Abioluz
print(lista[1:6])

#--4 Usando a indexação, escreva na tela uma lista com os seguintes dados:'
#      Cachorro grande é de arrasar, Abioluz, 80, abacaxi, amor, 20, 10'
print(lista[::-1])

#--5 Usando o f-string e a indexação escreva na tela os seguintes dados:'
#      '\n { abacaxi } é muito bom, sinto muito { amor } quando eu chupo { 80 }" deles.')
print(f'{lista[3]} é muito bom, sinto muito {lista[2]} quando eu chupo {lista[4]} deles.')

#-- 6: Usando a indexação, escreva na tela os seguintes dados
#      10, amor, 80, Cachorro grande é de arrasar')
print(lista[::2])

#--7 Usando o f-string e a indexação escreva na tela os seguintes dados:
#      'Abioluz - abacaxi - 10 - Cachorro grande é de arrasar - 20 - 80' )
print(f'{lista[5]} - {lista[3]} - {lista[0]} - {lista[-1]} - {lista[1]} - {lista[4]}')

#--8 Usando o f-string e a indexação escreva na tela os seguintes dados:'
#      amor - 10 - 10 - abacaxi - Cachorro grande é de arrasar - Abioluz - 10 - 20')
print(f'{lista[2]} - {lista[0]} - {lista[0]} - {lista[3]} - {lista[-1]} - {lista[5]} - {lista[0]} - {lista[1]}')

#--9 Usando a indexação, escreva na tela uma lista com dados de 10 até 80
print(lista[0:5])

#--10 Usando a indexação, escreva na tela os seguintes dados:
#      10, abacaxi, Cachorro grande é de arrasar')
print(lista[::3])






