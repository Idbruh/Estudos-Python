
#-- IMPORTAR BIBLIOTECA DO MySQL
import MySQLdb

def converter_tabela_dicionario(lista_tuplas):
    lista_pessoas = []
    for p in lista_tuplas:
        dicionario_pessoa = {'Id': 0, 'Nome': '', 'Sobrenome': '', 'Idade': 0, 'Endereco_ID': 0}
        print(p[0],p[1]) 
        dicionario_pessoa['ID'] = p[0]
        dicionario_pessoa['Nome'] = p[1]
        dicionario_pessoa['Sobrenome'] = p[2]
        dicionario_pessoa['Idade'] = p[3]
        dicionario_pessoa['Endereco_ID'] = p[4]
        lista_pessoas.append(dicionario_pessoa) 
    return lista_pessoas
























