# Aula 18 - 03-11-2019

# Ao receber a seguinte lista, faça um metodo que retorne cada um destes itens de forma individual 
# com cabaçalho dizendo em que posição estes itens estão dentro da lista principal:
# Exemplo: 
# ############# posição 0 ##################
# Agua
# mamão
# ############# posição 1 ##################
# banana
# limão

#Regra: Não pode usar a função range e no máximo 2 print()

lista = [#i
          ['mamão','abacaxi','laranja','uva','pera','maçã','vergamota'],
          ['skol','kaiser','sol','schin','brahma','itaipava','bavaria'],
          ['alface crespa', 'alface lisa','rucula','almerão','repolho','salsinha',],
          ['rizoto','macarronada','polenta','guizado','dobradinha','revirado','pure'],
          ['feijão', 'erviha', 'lentilha','vagem','feijão branco','gão de bico','soja'],
          ['agua','cachoeira','rio','lagoa','sanga','brejo','laguna'],
          ['vento','ciclone','tufão','furacão','brisa','minuano','zefiro'],
          ['carro','moto','vespa','caminhão','sprinter','kombi','fusca'],
          ['calça','camisa','japona','jaqueta','camiseta','bone','regata']
        ]

cont = 0

for i in lista:
  print('########## posição', cont, '######## ')
  cont = cont + 1
  for j in i:
    print(j)
  

'''
cont = 0

for i in lista:
  print('########## posição', cont, '######## ')
  cont = cont + 1
  for j in i:
    print(j)
    for k in j:
      print(k)'''






'''cab = (f'##### {lista[0]} ######')
dados = lista[0]

dic = {lista[0]}

for x in dados:
  dic = {}
  print(f'{cab[0]}')
  print(f'{dic[0]}')'''