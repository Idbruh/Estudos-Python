def exportar_txt(lista_pessoas):
    with open('Aula33/pessoas.txt','a') as arquivo: # com este comando n é necessário fechar o arquivo
        for p in lista_pessoas:
            arquivo.write(f"{p['ID']};{p['Nome']};{p['Sobrenome']};{p['Idade']};{p['Endereco_ID']}\n")