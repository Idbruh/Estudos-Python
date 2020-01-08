#Retira os viajantes do lado de partida
def embarque(opc1, opc2, lado):
    if opc1 == 1:
        lado.remove('missionario')
    elif opc1 == 2:
        lado.remove('canibal')
    if opc2 == 1:
        lado.remove('missionario')
    elif opc2 == 2:
        lado.remove('canibal')
    return lado

#Coloca os viajantes no lado destino
def desembarque(opc1, opc2, lado):
    if opc1 == 1:
        lado.append('missionario')
    elif opc1 == 2:
        lado.append('canibal')
    if opc2 == 1:
        lado.append('missionario')
    elif opc2 == 2:
        lado.append('canibal')
    return lado

#Neste método, será feita uma simulação de como vai ficar o lado de partida caso a viajem seja feita, validando se o canibal vai comer ou não.
def verificar_se_viagem_bem_sucedida(lado_esq, lado_dir, opc1, opc2, lado_partida):
    #Criando variáveis para saber quantos viajantes são missionários e canibais para utilizar na simulação.
    missionarios_barco = 0
    canibais_barco = 0

    #Determinando número de viajantes de cada tipo
    if opc1 == 1:
        missionarios_barco += 1
    elif opc1 == 2:
        canibais_barco += 1

    if opc2 == 1:
        missionarios_barco += 1
    elif opc2 == 2:
        canibais_barco += 1

    #Simulando se existem mais canibais do que missionários no lado de partida caso essa viajem seja feita.
    if lado_partida == 'esquerdo':
        if (lado_esq.count('missionario') - missionarios_barco) < (lado_esq.count('canibal') - canibais_barco):
            print('O canibal vai comer o missionário, favor selecionar novamente os viajantes do barco')
            return False
    elif lado_partida == 'direito':
        if (lado_dir.count('missionario') - missionarios_barco) < (lado_dir.count('canibal') - canibais_barco):
            print('O canibal vai comer o missionário, favor selecionar novamente os viajantes do barco')
            return False
    return True
        
#Não está completo, pois se tiver só 1 missionário ou 1 canibal e chamar 2 no barco, ele aceita.
def verifica_se_existe_viajante(lado_esq, lado_dir, lado_partida, opcao): 
    if lado_partida == 'esquerdo':
        if opcao == 1 and lado_esq.count('missionario') <= 0:
            print('Não existe um missionário disponível para viagem, portanto essa vaga do barco vai ficar vazia.')
            return False
        elif opcao == 2 and lado_esq.count('canibal') <= 0:
            print('Não existe um canibal disponível para viagem, portanto essa vaga do barco vai ficar vazia.')
            return False
        return True
    else:
        if opcao == 1 and lado_dir.count('missionario') <= 0:
            print('Não existe um missionário disponível para viagem, portanto essa vaga do barco vai ficar vazia.')
            return False
        elif opcao == 2 and lado_dir.count('canibal') <= 0:
            print('Não existe um canibal disponível para viagem, portanto essa vaga do barco vai ficar vazia.') 
            return False
        return True