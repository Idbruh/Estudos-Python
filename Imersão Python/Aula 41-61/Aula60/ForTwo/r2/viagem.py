from ForTwo.r2.embarque import embarque
from ForTwo.r2.desembarque import desembarque

from ForTwo.r2.terminal import Terminal
from ForTwo.r2.aviao import Aviao
from ForTwo.r2.local import Local
from ForTwo.r2.fortwo import Fortwo

terminal = {'descricao': 'terminal',
            'pessoas': ['piloto', 'oficial1', 'oficial2', 'chefe de serviço', 'comissário1', 'comissário2', 'policial',
                        'presidiario']}
aviao = {'descricao': 'aviao', 'pessoas': []}


def viagem(motorista: str, passageiro: str, saida: dict, chegada: dict):
    fortwo = embarque(motorista, passageiro, saida)
    print(f"Saindo do {saida['descricao']}")
    print('Iniciando a viagem...')
    print(f"Chegando no {chegada['descricao']}")
    print('Finalizando a viagem ...')
    # alto acoplamento
    desembarque(fortwo, chegada)
    print(saida)
    print(chegada)


def viagem2(pessoa1, pessoa2, origem: Local, destino: Local):
    fortwo = Fortwo()
    if origem.saida(pessoa2):
        if origem.saida(pessoa1):
            if fortwo.set_motorista(pessoa1):
                if fortwo.set_passageiro(pessoa2):
                    fortwo.viagem(origem, destino)
                    if destino.entrada(pessoa1):
                        if not destino.entrada(pessoa2):
                            print('Não permitido6')
                    else:
                        print('Não permitido5')
                else:
                    print('Não permitido4')
            else:
                print('Não permitido3')
        else:
            print('Não permitido2')
    else:
        print(f'Não o {pessoa1} viajar com o {pessoa2}')


avi = Aviao()
term = Terminal()

print('-----------------------------------------------\n')
viagem2('policial', 'presidiário', term, avi)
print('-----------------------------------------------\n')
viagem2('policial', '', avi, term)
print('-----------------------------------------------\n')
viagem2('piloto', 'policial', term, avi)
print('-----------------------------------------------\n')
viagem2('piloto', '', avi, term)
print('-----------------------------------------------\n')
viagem2('piloto', 'oficial1', term, avi)
print('-----------------------------------------------\n')
viagem2('piloto', '', avi, term)
print('-----------------------------------------------\n')
viagem2('piloto', 'oficial2', term, avi)
print('-----------------------------------------------\n')
viagem2('piloto', '', avi, term)
print('-----------------------------------------------\n')
viagem2('chefe de serviço', 'piloto', term, avi)
print('-----------------------------------------------\n')
viagem2('chefe de serviço', '', avi, term)
print('-----------------------------------------------\n')
viagem2('chefe de serviço', 'comissário1', term, avi)
print('-----------------------------------------------\n')
viagem2('chefe de serviço', '', avi, term)
print('-----------------------------------------------\n')
viagem2('chefe de serviço', 'comissário2', term, avi)
print('-----------------------------------------------\n')
