#incluido comentários no código: use "#" ou ''' para comentario longo
#Revisar concatenação
#Realiza as 4 operações
#Fazer programa que leia 2 numeros
#Imprima o resultado das operações
#Diga qual numero é o maior dos dois numeros


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