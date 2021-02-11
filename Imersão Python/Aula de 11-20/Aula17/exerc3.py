#Faça um programa que leia um numero inteiro de 1 a 100 no teclado e
# mostre se você acertou ou
# o numero digitado é maior ou menor
# quando voce acertar o programa deve ser finalizado


from random import randint
aleatorio = randint(1,10)
'''
num = 0

while True:
    num = int(input('Digite um numero: '))
    if num == aleatorio:
        print('Acertou.. O numero é igual ao aleatorio')   
        break
    elif num < aleatorio:
        print('Errou... o numero digitado é menor que o aleatorio.. Tente outra vez')  
    elif num > aleatorio:
        print('Errou... o numero digitado é maior que o aleatorio.. Tente outra vez')  '''


#-- Resolução Abioluz
print(aleatorio)
numero = 0
while not numero == aleatorio:
    numero = int(input('Digite um numero: '))
    if numero > aleatorio:
        print('O numero é maior que.. tente outra vez.')
    elif numero < aleatorio:
        print('O numero é menor que.. tente outra vez.')
    else:
        print('Você acertou..')

    








