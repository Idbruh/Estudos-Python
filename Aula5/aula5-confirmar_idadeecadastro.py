#2-
#Mercado Tech -----
#Solicitar Nome do Funcionario
#Solicitar idade
#Informar se o funcionario pode adquirir produtos alcoolicos

#3-
#Cadastro de produtos Mercado tech
#Solicitar o nome do produto
#Solicitar a categoria do produto (alcoolicos e não alcoolicos)
#exibir produto cadastrado

#2-

print('=' *50)
print('Mercado Tech')
nome = input('Digite o seu nome: ')
idade = int(input(f'Olá {nome}, agora digite a sua idade: '))

categoria1 = 1
categoria2 = 2

if idade >= 18:
    print('Você tem autorização para comprar alcoolicos!') 
    #int(input('Digite ', 1, ' para continuar: '))
else:
    print('Voce não pode comprar alcoolicos!')

print('Mercado Tech Produtos')

if idade >= 18:
    print('Alcolicos')
else:
    print('Não alcoolicos')




