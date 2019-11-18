#--- Exercicio 2  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia os dados de um cliente
#--- Cliente: Nome, Sobrenome, ano de nascimento
#--- Exiba uma mensagem de boas vindas para o cliente
#--- Exiba um menu: Produtos alcoolicos e Produtos não alcoolicos, Sair
#--- Caso o cliente seja menor de idade o item 'produtos alcoolicos' não deve ser exibido
#--- Leia a opção digitada e crie uma tela para cada opção



print('=' *50)
print('\nMercado Tech')
nome = input('\nDigite o seu nome: ')
idade = int(input(f'Olá {nome}, agora digite a sua idade: '))


print('\n'f'Bem vindo {nome}\n')

if idade <= 18:
    escolhe = int(input('Qual menu você deseja acessar? 1- Produtos Alcoolicos 2- Produtos Não Alcoolicos 3-Sair: '))
    if escolhe == 1:
        print('Cerveja Bhrama: $2,00 | Cerveja Original 1l: R$3,00.')
    elif escolhe == 2:
        print('Guaraná Antartica 250ml: $1,25,00 / Sprite 2l: $4,00 / Energético: $4,50.')
    elif escolhe ==3:
        print:('Volte sempre!')
else:
    escolha = int(input('Qual tipo de produtos você deseja comprar? 1. Produtos sem Alcool 2. Produtos sem Alcool ou 3. Sair: '))
    if escolha == 1:
        print('Guaraná Antartica 250ml: $1,25,00 / Sprite 2l: $4,00 / Energético: $4,50.')
    elif escolhe == 2:
        if escolha == 3:
            print:('Volte sempre!')