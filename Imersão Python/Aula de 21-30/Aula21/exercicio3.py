# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um metodo que leia 5 valores inteiros e retorne uma lista.
# Esta função deve ter tratamento de excessão evitando erro ValueError.

# 2 - Com a lista retornada, faça a multiplicação por 5 e salve o resultado
# em outra lista.

# Imprima a lista resultante


lista_num = []
resul = []
posicao = 1

quant = 5
try:
    for i in range(quant):
        numero = int(input(f'Digite a {posicao} número: '))
        lista_num.append(numero)
        posicao += 1
    for j in  lista_num:
        multi = j * 5
        resul.append(multi)
    

    print(f'O resultado da multiplicação dos numeros é {resul}.')

except ValueError:
    print('Digite apenas números inteiros.')
    

