#técnica
    # 'piloto',
    # 'oficial1',
    # 'oficial2'
#cabine
    #'chefe de serviço'
    #'comissário1'
    #'comissário2'
#passageiros
    #'policial'
    #'presidiario'


terminal = {'descricao':'terminal', 'pessoas': ['piloto','oficial1','oficial2','chefe de serviço','comissário1','comissário2','policial','presidiario']}
aviao = { 'descricao':'aviao', 'pessoas': [] }


def viagem(motorista:str, passageiro:str, saida:dict, chegada:dict):
    fortwo = embarque(motorista, passageiro, saida)
    print(f"Saindo do {saida['descricao']}")
    print('Iniciando a viagem...')
    print(f"Chegando no {chegada['descricao']}")
    print('Finalizando a viagem ...')
    # alto acoplamento
    desembarque(fortwo, chegada)
    print(saida)
    print(chegada)

def embarque(motorista:str, passageiro:str, saida:dict):
    fortwo = {'motorista': motorista, 'passageiro': passageiro}
    saida['pessoas'].remove(motorista)
    print(f"{fortwo['motorista']} embarcou como motorista")

    if passageiro != '':
        saida['pessoas'].remove(passageiro)
        print(f"{fortwo['passageiro']} embarcou como passageiro")

    return fortwo

def desembarque(fortwo:dict, chegada:dict):
    print(f"{fortwo['motorista']} desembarcou")
    chegada['pessoas'].append(fortwo['motorista'])
    fortwo['motorista'] = ''

    if fortwo['passageiro'] != '':
        print(f"{fortwo['passageiro']} desembarcou")
        chegada['pessoas'].append(fortwo['passageiro'])
        fortwo['passageiro'] = ''


viagem('policial','presidiario', terminal, aviao)
viagem('policial','', aviao, terminal)
viagem('piloto','policial', terminal, aviao)
viagem('piloto','', aviao, terminal)
viagem('piloto','oficial1', terminal, aviao)
viagem('piloto','', aviao, terminal)
viagem('piloto','oficial2', terminal, aviao)
viagem('piloto','', aviao, terminal)
viagem('chefe de serviço','piloto', terminal, aviao)
viagem('chefe de serviço','', aviao, terminal)
viagem('chefe de serviço','comissário1', terminal, aviao)
viagem('chefe de serviço','', aviao, terminal)
viagem('chefe de serviço','comissário2', terminal, aviao)

################################ B R U N A #############################################

#-tripulação tecnica
    # 'piloto'
    # 'oficial1'
    # 'oficial2'
#-cabine
    # 'chefe de serviço'
    # 'comissário1'
    # 'comissário2'
#-passageiros
    # 'policial'
    # 'presidiário'


#
#
# terminal = {'descricao': 'terminal', 'pessoas':  ['piloto', 'oficial1', 'oficial2', 'chefe de serviço', 'comissário1', 'comissário2', 'policial', 'presidiário']}
# aviao = {'descricao': 'aviao', 'pessoas': []}
# fortwo = {'motorista': '', 'passageiro': ''}
#
#
# def retirar(item, lista:list):
#     lista.remove(item)
#
# def inserir(item, lista: list):
#         lista.append(item)
#
# def viagem(motorista:str, passageiro:str, saida:dict, chegada:dict):
#     fortwo = embarque(motorista, passageiro, saida)
#     print(f"Saindo do {saida['descricao']}")
#     print('Iniciando a viagem...')
#     print(f"Chegando do {chegada['descricao']}")
#     print('Finalizando a viagem...')
#     return desembarque(fortwo, chegada)
#     #alto acoplamento
#
#
# def embarque(motorista:str, passageiro:str, saida:dict):
#     saida['pessoas'].remove(motorista)
#     saida['pessoas'].remove(passageiro)
#     fortwo = {'motorista':  motorista, 'passageiro': passageiro}
#     print(f"{fortwo['motorista']} embarcou como motorista")
#     print(f"{fortwo['passageiro']} embarcou como passageiro")
#     return fortwo
#
# def desembarque(fortwo:dict, chegada:dict):
#     print(f"{fortwo['passageiro']} desembarcou")
#     print(f"{fortwo['motorista']} desembarcou")
#     chegada['pessoas'].append(fortwo['motorista'])
#     chegada['pessoas'].append(fortwo['passageiro'])
#     fortwo['motorista'] = ''
#     fortwo['passageiro'] = ''
#
#
# viagem('policial', 'presidiario', terminal, aviao)
