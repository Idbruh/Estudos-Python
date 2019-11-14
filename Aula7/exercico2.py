# Exercicio 2- Dicionarios
# Escreva um programa que leia os dados de 11 jogadores
# jogador: nome, posicao, numero, time
# crie um dicionario para armazenar os dados
# imprima todos os jogadores e seus dados



lista_jogadores = []
for i in range(0,2):
    dicionario_jogadores = {}
    dicionario_jogadores['Nome'] = input('Digite o Nome: ')
    dicionario_jogadores['Posicao'] = input('Digite o Posicao: ')
    dicionario_jogadores['Numero'] = input('Digite o Numero: ')
    dicionario_jogadores['Time'] = input('Digite o Time: ')
    lista_jogadores.append(dicionario_jogadores)

for j in lista_jogadores:
    print(f"{j['Nome']} - {j['Posicao']} - {j['Numero']} - {j['Time']}")
