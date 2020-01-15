# -- Classes

#-- classe é uma estrutura(conjunto) de dados e comportamentos (evolução dos dicionarios)

#-- IMPORTAR BIBLIOTECA DO MySQL
import MySQLdb

#-- configurar uma conexao
conexao = MySQLdb.connect(host= "127.0.0.1", database='bruna-aula31-db', user='root', passwd= '')

#-- SALVA O CURSOR DA CONEXÃO EM UMA VARIAVEL
cursor = conexao.cursor()

#-- CRIACAO DO DICIONARIO QUE REPRESENTA UMA PESSOA
dicionario_pessoa = {'Id': 0, 'Nome': '', 'Sobrenome': '', 'Idade': 0, 'Endereco_ID': 0}
lista_pessoas = [] # cria uma lista vazia

#-- CRIACAO DO COMANDO SQL E PASSANDO PARA O CURSOR
comando_sql_select = "SELECT * FROM pessoa"
cursor.execute(comando_sql_select)

resultado = cursor.fetchall()  #(aqui ele vai retornar uma tupla ou uma lista de tuplas, para pegar o resultado usar o FOR)
for p in resultado:
    dicionario_pessoa = {'Id': 0, 'Nome': '', 'Sobrenome': '', 'Idade': 0, 'Endereco_ID': 0} # toda vez que cair no for ele recria uma area de memoria e recria os valores.
    # Apesar da variavel ter o mesmo nome ele vai ser redirecionado a outra área memoria
    print(p[0],p[1]) # imprime a primeira e segunda posição da tupla
    dicionario_pessoa['ID'] = p[0]
    dicionario_pessoa['Nome'] = p[1]
    dicionario_pessoa['Sobrenome'] = p[2]
    dicionario_pessoa['Idade'] = p[3]
    dicionario_pessoa['Endereco_ID'] = p[4]
    lista_pessoas.append(dicionario_pessoa)   # adiiona do dicionario + lista vazia


#-- Abre um arquivo .txt e salva as informaçoes do dicionario percorrendo a o dicionario e atribuindo a uma posição, salvando no formato pre-definido
with open('Aula33/pessoas.txt','a') as arquivo: # com este comando n é necessário fechar o arquivo

    for p in lista_pessoas:
        #print(f'\t {p} ')
        arquivo.write(f"{p['ID']},{p['Nome']},{p['Sobrenome']},{p['Idade']},{p['Endereco_ID']}\n")






























