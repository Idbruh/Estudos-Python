lista =  [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
# Indice  0, 1, 2, 3, 4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19

# Para selecionar um item isolado de uma lista
print(lista[10])
# o resultado é: 15

# Para pegar uma fatia da lista do 15 a 20
# tem que ter atenção que o segundo indice não inclui o elemento anterior.
print(lista[10:15])
# o resultado é:[15, 16, 17, 18, 19]
#Para consegui a lista de 15 a 20 deve se adicionar +1 no valor do seguindo indice
print(lista[10:16])
# o resultado é: [15, 16, 17, 18, 19, 20]

# Para resgatar o ultimo elemento do indice, pode-se usar o -1
print(lista[-1])
# o resultado é: 24

# Há mais um indice que pode fatiar os elementos 
# inteirando de 2 em 2... 3 em 3..., 
print(lista[10:17:3])
# o resultado é: [15, 18, 21]

#Para fatiar os elementos de uma determinada posição até o final da lista pode-se usar o : 
print(lista[10:])
# o resultado é: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
