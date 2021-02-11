#2- Faça um menu interativo que tenha:
#-- Cadastro de bandas, cadastro do album,
# cadastro da musica e sair.  
#-- O menu deve ser executado até que se escolha
#  a opção sair.
#-- Cada opção deve ser mostrada
#-- Quando selecionada a opção sair, deverá aparecer
# na tela as informações das bandas, albuns e musicas
# 
# 
#  
c_banda = []
c_album = []
c_musica = []


menu = '''
----------------------------------------------------
            C A D A S T R O
----------------------------------------------------
1. Cadastro de B A N D A
2. Cadastro de A L B U M 
3. Cadastro de M U S I C A
-----------------------------------------------------
4. S A I R 
-----------------------------------------------------
'''
while True:
    opcao = input(menu)
    if opcao == '1':
        c_banda.append(input('Cadastre a B A N D A:\n'))
    elif opcao == '2':
        album = input('Cadastre o A L B U M:\n')
        c_album.append(album)
    elif opcao == '3':
        musica = input('Cadastre a M U S I C A:\n')
        c_musica.append(musica)
    elif  opcao == '4':
        print(f'Você está deixando o sistema. Veja abaixo os dados cadastrados: \n1. Banda: {c_banda}\n2. Album: {c_album}\n3. Musica:{c_musica}')
        break
    else:
        print('Valor inválido')


#  - Resolução Abioluz - 
#-- primeiro cria as listas
#-- depois cria o menu com opções 
#-- cria um while true e pede a opção do menu
#-- cria condições de  if e   c_banda.append('Digite o nome da banda: ')
# 
#   

