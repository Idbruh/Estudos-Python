# Criar um programa para cadastro de cliente
# Para cadastro de cliente deve pedir os seguintes dados:
# codigo de cliente, CPF nome e endereço
# data de nascimento, estado, cidade, cep, bairro, rua
#  numero da casa, complemento



def cadastro_cliente(num_funcao):
    dados_clientes = ['codigo_cliente: ', 'CPF: ', 'nome_completo: ', 'data_nascimento: ', 'estado: ',
                    'cidade: ','cep: ', 'bairro: ', 'rua: ', 'n_casa: ','complemento: ']

    lista = []
    for h in range(num):
        dicionario = {}

        for i in dados_clientes:
            dicionario[i] =  input(f'{i}')

        lista.append(dicionario)
    return lista

num = int(input('Digite quantos cadastros você vai fazer: '))

lista_cadastro = cadastro_cliente(num)


arquivo = open('Aula17/cliente_ex4.txt','a')
for cliente in arquivo:
    cliente_chave = list(cliente.keys())
    for chaves in cliente_chave:
        salvar = (f'{cliente[chaves]}')

arquivo.write()
arquivo.close()


    