from bla import *
lado_esq = ['missionario','missionario','missionario','canibal','canibal','canibal']
lado_dir = []
lado_partida = 'esquerdo'



opc = 0
while opc != 7:

    menu1 =('''
==============================================
=............................................=
=      J O G O: CANIBAIS & MISSIONÁRIOS      =
=............................................=
==============================================
= 1. MISSIONARIO                             =
=............................................=
= 2. CANIBAL                                 =
=............................................=
= 3. NINGUEM                                 =
=............................................=
==============================================
=............................................=
= 7. SAIR                                    =
=............................................=
==============================================

''')
    
    opc1 = int(input('\nEscolha quem vai embarcar 1*, pelo numero: '))
    if opc1 == 7:
        print('Você saiu do jogo, até mais.')
        break
    opc2 = int(input('Escolha quem vai embarcar 2*, pelo numero: '))
    if opc2 == 7:
        print('Você saiu do jogo, até mais.')
        break
    if not opc1 in (1, 2, 3, 7) and not opc2 in (1, 2, 3, 7):
        print('Opção inválida, retornando para a primeira pergunta.')
    else:
        if opc1 == 1:
            if verifica_se_existe_viajante(lado_esq, lado_dir, lado_partida, 1) == False:
                opc1 = 3
            else:
                print('Missionário escolhido')
        else:
            if verifica_se_existe_viajante(lado_esq, lado_dir,lado_partida, 2) == False:
                opc1 = 3
            else:
                print('Canibal escolhido')
        if opc2 == 2:
            if verifica_se_existe_viajante(lado_esq, lado_dir,lado_partida, 2) == False:
                opc2 = 3
            else:
                print('Canibal escolhido')
        else:
            if verifica_se_existe_viajante(lado_esq, lado_dir,lado_partida, 1) == False:
                opc2 = 3
            else:
                print('Missionário escolhido')

        if verificar_se_viagem_bem_sucedida(lado_esq, lado_dir, opc1, opc2, lado_partida) == True:
            if lado_partida == 'esquerdo':
                lado_esq = embarque(opc1, opc2, lado_esq)
                lado_dir = desembarque(opc1, opc2, lado_dir)
            else:
                lado_dir = embarque(opc1, opc2, lado_dir)
                lado_esq = desembarque(opc1, opc2, lado_esq)
            if lado_partida == 'esquerdo':
                lado_partida = 'direito'
            else:
                lado_partida = 'esquerdo'
            if lado_dir.count('missionario') == 3 and lado_dir.count('canibal') == 3:
                print('Parabéns, você venceu o jogo.')
                break


#resolução

#leva 2 canibais
#volta 1 canibal
#leva 2 canibais
#volta um canibal
#leva 2 missionário
#volta 1 canibal e 1 missionário
#leva 2 missionario
#volta canibal
#leva 2 canibais
#volta canibal
#leva 2 canibais






