def viagem_carro(motorista, passageiro,horario_partida,previsao_chegada):
    arquivo = open('viagemC.txt','a')
    arquivo.write(f'{motorista};{passageiro};{horario_partida};{previsao_chegada}\n')
    arquivo.close
    return print('\nRegistro de viagem com o veículo: F O U R T W O  concluído!\n')



def ler_viagensC():
    lista_viagensC = []
    arquivo = open('viagemC.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        lista_completaC = linha.split(';')
        dicionario_viagensC= {'Motorista':lista_completaC[0], 'Passageiro':lista_completaC[1], 'Horario de Partida':lista_completaC[2], 'Previsão de Chegada':lista_completaC[3]}
        lista_viagensC.append(dicionario_viagensC)
        arquivo.close
    return lista_viagensC



def salvar_pessoas_terminal(elemento_id,nome_pessoa):
    arquivo = open('pessoasT.txt','a')
    arquivo.write(f'{elemento_id};{nome_pessoa};\n')
    arquivo.close
    return print('Cadastro de embarque no  T E R M I N A L  concluido!')

def ler_pessoas_terminal():
    arquivo = open('pessoasT.txt','r')
    lista_pessoasT = []
    for linha in arquivo:
        linha = linha.strip()
        lista_pessT = linha.split(';')
        dicionario_pessoasT = {'Elemento de Identificação':lista_pessT[0], 'Nome Pessoa':lista_pessT[1]}
        lista_pessoasT.append(dicionario_pessoasT)
        arquivo.close
    return lista_pessoasT



def salvar_pessoas_aviao(elemento_id, nome_pessoa):
    arquivo = open('pessoasA.txt','a')
    arquivo.write(f'{elemento_id};{nome_pessoa};\n')
    arquivo.close
    return print('Cadastro de embarque no  A V I Ã O  concluido!')

def ler_pessoas_aviao():
    arquivo = open('pessoasA.txt','r')
    lista_pessoasA = []
    for linha in arquivo:
        linha = linha.strip()
        lista_pessA = linha.split(';')
        dicionario_pessoasA = {'elemento_id':lista_pessA[0], 'nome_pessoa':lista_pessA[1]}
        lista_pessoasA.append(dicionario_pessoasA)
        arquivo.close
    return lista_pessoasA 