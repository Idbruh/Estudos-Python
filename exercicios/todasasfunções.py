print('\n................................................................................')
print('..........................========..............................................')
print('.................-=====================+........................................')
print('................-====  =================-.......................................')
print('................:==      ================+......................................')
print('................:====  ==================+......................................')   
print('................:========================+......................................')
print('.............................*===========+......................................')
print('.......+=================================+.*=======:............................')
print('.....+===================================+.*======..............................')
print('....+====================================+.*=========*..........................')
print('...-=====================================:-===========-.........................')
print('...+====================================:.*===========+.........................')
print('...*=================================*-.:=============*.........................')
print('...*==============:..---------------:+=================.........................')
print('...+============:.:===================================*.........................')
print('...:===========:.*====================================+.........................')
print('....*==========.:=====================================..........................')
print('....-==========.:====================================-..........................')
print('.....-*========.:===================================-...........................')
print('........-++++++.:============++++++++++++++++++++:..............................')
print('................:============............:......................................')
print('...............:=========================.......................................')
print('................:==================  =====......................................')
print('................-================      ==:......................................')
print('................-================      ==:......................................')
print('.................-=================  ===-.......................................')
print('...................:*================...........................................')
print('..........................========..............................................')
print('................................................................................')
print('...........................V E N D A   D E   B E B I D A S  A Q U I !...........\n')
print('-.-.'*20)

usuario = ('sudo')
senha = ('root')

login = input('Digite o seu usuário: ')
pawrd = input('Digite a sua senha: ')

if login == usuario and  pawrd == senha:
    print('Logado com sucesso!','\n S E J A   B E M   V I N D X!\n')
else:
    print('Usuario e/ou senha incorretos!')

print('-.-.'*20)

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