#--- Exercicio 1  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia dois números inteiros
#--- Realize as 4 operações matemáticas básicas com os números lidos
#--- Imprima os resultados das operações 
#--- Informe qual número é maior ou se os dois são iguais


num1 = int(input('1º número: '))
num2 = int(input('2º número: '))


soma = num1 + num2
sub = num1 - num2
div = num1 / num2
multi = num1 * num2

print('Soma: ', soma, 'Subtração: ', sub, 'Divisão: ', div, 'Multiplicação: ', multi)
if num1 < num2:
     print('O n° 1 é menor.')
elif num1 == num2:
    print('Os dois números são iguais.')
else:
    print('O nº 2 é maior.')