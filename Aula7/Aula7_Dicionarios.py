# #aula - 7
# #Dicionarios

# '''lista = [] #composta por colchetes
# dicionario = {} #composto or chaves, semelhante a lista..para cada dado ao invés de ser mutavel ele irá buscar o valor que esá definido nas chaves'''

# #dicionario ={ chave:valor, chave: valor}

# '''dicionario = {'Nome': 'Bruna', 'Sobrenome': 'Carmo'}
# print(dicionario)
# print(dicionario['Sobrenome'])'''

# nome = "Mirella"
# lista_notas = [10,20,30,40]
# media = sum(lista_notas)/ len(lista_notas) #sum: soma todos o conteudo de uma lista // len: divide pela quantidade de elementos tem na lista
# situacao = 'Reprovado'
# if media>=7:
#     situacao = 'Aprovado'
# dicionario_alunos = {'Nome':nome, 'Lista_Notas':lista_notas, 'Média':media, 'Situação':situacao}

# print(f"{dicionario_alunos['Nome']} - {dicionario_alunos['Situação']}")

dicionario_bandas = {}
dicionario_bandas['Nome'] = 'Calipso'
print(dicionario_bandas)

#ou

dicionario_bandas2 = {'Nome': ''}
dicionario_bandas2['Nome'] = 'Deja vu'
print(dicionario_bandas2)

#ou

dicionario_nome ={'Nome':'Joana', 'Sobrenome':'aloka' }
dicionario_nome['Sobrenome'] = 'Surtada'
dicionario_nome['CPF'] = '08366333930'
print(dicionario_nome)
