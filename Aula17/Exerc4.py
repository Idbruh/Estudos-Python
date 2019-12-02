# Criar um programa para cadastro de cliente
# Para cadastro de cliente deve pedir os seguintes dados:
# codigo de cliente, CPF nome e endereço
# data de nascimento, estado, cidade, cep, bairro, rua
#  numero da casa, complemento

num = int(input('Digite quantos cadastros você vai fazer: '))


def cadastro_cliente():
    dados_clientes = ['codigo_cliente: ', 'CPF: ', 'nome_completo: ', 'data_nascimento: ', 'estado: ',
                    'cidade: ','cep: ', 'bairro: ', 'rua: ', 'n_casa: ','complemento: ']

    lista = []

    for h in range(num):
        dicionario = {}

        for i in dados_clientes:
            dicionario[i] =  input(f'{i}')

        lista.append(dicionario)


cadastro_cliente()
