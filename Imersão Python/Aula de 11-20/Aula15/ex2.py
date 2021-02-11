#-- Exercico 2
# definir marca , tipo, teor alcoolico


def salvar_cerveja(cerveja_dicionario):
    arquivo = open('exercicio2.txt','x')
    arquivo.write(f"{cerveja_dicionario['marca']};{cerveja_dicionario['tipo']};{cerveja_dicionario['teor']}\n")
    arquivo.close()


def ler():
    lista = []
    arquivo = open('exercicio2.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        cerveja = {'marca':lista_linha[0],'tipo':lista_linha[1],'teor':lista_linha[2]}
        lista.append(cerveja)
    arquivo.close()
    return lista


marca = input('Digite a marca cerveja: ')
tipo = input('Defina o tipo da cerveja: ')
teor = float(input('Digite o teor alcoolico: '))


cerveja = {'marca':marca,'tipo':tipo,'teor':teor}
salvar_cerveja(cerveja)

for x in ler():
    print(f"{x['marca']} - {x['tipo']} - {x['teor']}")