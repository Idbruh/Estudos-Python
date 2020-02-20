from FORTWO.RESOLUCAO2.embarque import embarque
from FORTWO.RESOLUCAO2.desembarque import desembarque

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