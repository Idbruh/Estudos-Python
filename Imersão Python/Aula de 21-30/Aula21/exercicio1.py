# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um arquivo que leia 2 números inteiros e imprima a soma, 
# multiplicação, divisão e subtração com uma f-string.

# 2 - Crie um while que pergunte se deseja continuar. Se digitar 's' o
# programa termina.

#################### até aqui tudo bem! ##########################

# 3 - faça um tratamento de exceção para que ao digitar o valor que 
# não seja inteiro, ele avise o usuário para ele digitar denovo.
# 4 - Faça outro tratamento de exceção para evitar que divida um numero
# por zero.


controle = 'n'


while True:
    try:
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
        print(f'A soma entre {n1} e {n2} é: {n1 + n2}')
        print(f'A diferença entre {n1} e {n2} é: {n1-n2}')
        print(f'A mutiplicação entre {n1} e {n2} é: {n1*n2}')
        if n2 == 0:
            try:
                print(f'A divisão entre {n1} e {n2} é: {n1 / n2}')
            except ZeroDivisionError:
                    print('Não é possivel dividir por zero')
        

    except ValueError:
        print('Você digitou uma letra, animal!\nDigite um numero inteiro, sem virgulas ou ponto')
    

    else:
        print('Fim!')            
        break

# while controle!= 's' and True:
#     try:
#         print('Digite apenas numeros')   
#     n1 = int(input('Digite o primeiro numero: '))
#     n2 = int(input('Digite o segundo numero: '))
#     print(f'A soma entre {n1} e {n2} é: {n1 + n2}\nA diferença entre {n1} e {n2} é: {n1-n2}\nA mutiplicação entre {n1} e {n2} é: {n1*n2}\nA divisão entre {n1} e {n2} é: {n1/n2} ')
#     except ValueError:
#         print('Voce digitou letras... é somente numeros...')
#     controle = input("Digite 'n' para ficar e 's' para sair: ")
    
#     else:
#         print('Fim!')            
#         break