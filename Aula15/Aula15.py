#-- Módulo 15 - 28-11-2019
#-- Manipulação de arquivos
#-- dar o nome ao metodo "aula15.txt" | 'x' = abrir criar arquivo e abre para escrita | 'w' - escreve
#-- abrir paramentro e salvar na variavel 'arquivo'
#-- função write = escrever algo no arquivo
#-- \n concatena em cada linha para ele ir salavando os novos dados

'''arquivo = open('aula15.txt','a')
arquivo.write('Voltolini\n')
arquivo.close()'''

'''arquivo = open('aula15.txt', 'r')
for linha in arquivo:
    print(linha)
arquivo.close()'''

#-- salvar dados como dicionário -- ';' = pula para a proxima linha separando os dados

'''nome = input('Digite nome: ')
sobrenome = input('Digite sobrenome: ')
idade = int(input('Digite idade: '))
arquivo = open('aula15.txt','a')
pessoa = f'{nome};{sobrenome};{idade}\n'

arquivo.write(pessoa)
arquivo.close()'''


#-- incluindo metodo
def salvar_pessoa(pessoa_dicionario):
    arquivo = open('Aula15/aula15.txt','a')
    arquivo.write(f"{pessoa_dicionario['nome']};{pessoa_dicionario['sobrenome']};{pessoa_dicionario['idade']}\n")
    arquivo.close()

#restorno desta função terá todos os itens da minha lista
def ler():
    lista = []
    arquivo = open('aula15.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        pessoa = {'nome':lista_linha[0],'sobrenome':lista_linha[1],'idade':lista_linha[2]}
        lista.append(pessoa)
    arquivo.close()
    return lista


nome = input('Digite nome: ')
sobrenome = input('Digite sobrenome: ')
idade = int(input('Digite idade: '))
arquivo = open('aula15.txt','a')
pessoa = {'nome':nome, 'sobrenome':sobrenome, 'idade':idade}
salvar_pessoa(pessoa)


for p in ler():
    print(f"{p['nome']} - {p['sobrenome']} - {p['idade']}")


#-- primeiro: define as variaveis com input
#-- segundo: define um dicionários para armazenar os dados das variaveis separando os
#   itens por ';' para evitar conflitos
#-- criar uma metodo ( def ler(): ) e  cria uma lista de string ( lista = [] ) e 
#   usa .append na variavel definida pelo for [ex: for linha in arquivo --> lista.append(linha)]
#   fecha o arquivo e retorna a lista (return lista) 
#-- ler a função definida (--  print (ler() ) --) 
#-- stirp tira os espaços em branco no final e no começo, e tbm o '\n' salvando o resultao na propria linha
#-- criar outra variavel(lista_linha) procura pelo caractere definido';' e quebre a linha 
# armazenar variavel em uma lista




