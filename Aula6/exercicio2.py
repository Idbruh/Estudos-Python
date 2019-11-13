#-- E X E R C I C I O   1-  Listas
#Escreva programa que leia um numero inteiro
#Calcule a taboada do numero informado
#imprima a taboada completa

numero = int(input('Digite um numero: '))

for i in range(0,11):
    print(f'{i} x {numero} = {i*numero}')
