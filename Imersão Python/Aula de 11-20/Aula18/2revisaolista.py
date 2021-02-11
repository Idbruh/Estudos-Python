# Lista dentro de outra lista

lista = [3,4,5,[9,10,11],20,30]
print(lista)
# O resultado é: [3, 4, 5, [9, 10, 11], 20, 30]

#Para acessar o numero 9 dentro desta lista:
print(lista[3][0])
# O resultado é: 9

# Para acessar o numero 300 desta lista:
lista =[3, 4, 5, [9, [80,90,100,[200,300,400]], 11], 20, 30]
# Primeiro devemos acessar o indice que contêm a lista interna
print(lista[3])
# O resultado é: [9, [80, 90, 100, [200, 300, 400]], 11]

# Ir acessando item por item da lista:
print(lista[3][1])
# O resultado é: [80, 90, 100, [200, 300, 400]]
print(lista[3][1][3])
# O resultado é: [200, 300, 400]
print(lista[3][1][3][1])
# O resultado é: 300

# Nota-se que cada conchetes adicionado com o indice da lista, 
# entramos cada vez mais para dentro das listas.