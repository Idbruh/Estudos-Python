#---- Exercicio 1 - Dicionario
#---- Escreva programa que leia os dados de cerveja
#---- Cerveja: Marca, Tipo, IBU, ABV, EBC, Volume
#---- Crie um dicionario para armazenar os dados
#---- Imprima os dados do dicionario (não dicionario completo)



cerveja = {}
cerveja['nome'] = input('Digite o nome da Cerveja: ')
cerveja['tipo'] = input('Digite o tipo da cerveja: ')
cerveja['IBU'] = float(input('Digite o IBU da cerveja: '))
cerveja['ABV'] = float(input('Digite o IBU da cerveja: '))
cerveja['EBC'] = float(input('Digite o EBC da cerveja: '))
cerveja['Volume'] = float(input('Digite o Volume da cerveja: '))


print(f"{cerveja['nome']}\n {cerveja['tipo']}\n {cerveja['IBU']}\n {cerveja['ABV']}\n {cerveja['EBC']}\n {cerveja['Volume']}")


#----jeito talissa

