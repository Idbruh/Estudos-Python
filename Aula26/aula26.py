# -- Laços de repetição

# for contador in range(1,10):
#     passo
# pega_maçã

# for contador in range(0,3):
#     passo
#     pula
# passo
# pega_maçã

# for contador in range(0,3):
#     if moeda:
#         pega
#     passo
#     pula
# passo 
# pega_maçã

# print('oi')
# print('---'*10)


# for i in range(0,6):
#     print('oi')
# print('fim')

# print('---'*10)
# for i in range(0,6):
#     print(i)
# print('fim')

# print('---'*10)
# for i in range(6,0,-1):
#     print(i)
# print('fim')
# print('---'*10)
# print('---'*10)

# n = int(input('Digite um numero: '))

# for i in range(0,n+1):
#     print(i)
# ______________________________________

# contador = 1
# while contador <10:
#     print(contador)
#     contador += 1
# print('fim')


n = 1
# while n != 0:
#     n = int(input('Digite um numero: '))
# print('fim')

# r = 'S'
# while n != 0:
#     n = int(input('Digite um numero: '))
#     r = str(input('Quer continuar? [ S / N ]\n')).upper()
# print('fim')

# par = impar = 0
# while n != 0:
#     n = int(input('Digite um numero: '))
#     if n % 2 == 0:
#         par += 1
#     else:
#         impar += 1
 
# print('vc digitou {} pares e {} impares'.format(par,impar))



import time

for i in range(0,10):
    time.sleep(1)
    print(i)