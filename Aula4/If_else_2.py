#--- Aula 4 - IF & Else 2
print('-------------------------------')
lista_numeros = [1,2,3]
numero = 4

if 'Teti'.count("t") > 0:
    print('Existe "t" em "Teti" ')

if 'e'in 'Teti':
    print('Existe "t" em "Teti" ')

if 'M'not in 'Teti':
    print('Não existe "M" em "Teti" ')
if numero in lista_numeros:
    print('Existe "t" em "Teti" ')

if ''not in 'Teti':
    print('Existe ') 
else:
    print('Não existe ') 

lista_vazia = []
lista_nomes = ['Teti', 'Marcela', 'aaaa']
print('-------------------------------')

if len(lista_numeros) ==0:
    print('Vazia')
else:
    print('Não Vazio')

fraZe = ''
#ou
print('-------------------------------')
if lista_vazia:
    print('Vazia')

if lista_nomes:
    print( 'tem nomes')
else:
    print('n tem nomes')
print('-------------------------------')
nome = ''
if nome:
    print('Preenchido')
else:
    print('Vazia')
print('-------------------------------')

nome = ''
print(nome)
nome = 'Bru'
print(nome)
print(nome[2])
#string é imutavel: n é possivel alterar valor para uma variavel pré definida(string se comporta como uma lista ou tupla)
print('-------------------------------')   


