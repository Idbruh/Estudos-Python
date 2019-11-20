#--- Aula 9
#--- crie um programa que:
# --- 1. leia dois numeros inteiros
# --- Calcule a soma entre os dois atraves de um metodo
# ---Calcule a subtração entre os dois atraves de um metodo
# ---Calcule a multiplicação entre os dois atraves de um metodo
#--- Calcule a divisão interira entre os dois atraves de um metodo
# ---Calcule a divisão fracionada entre os dois atraves de um metodo
# ---Calcule o resto da divisão entre os dois atraves de um metodo
#--- Calcule a raiz entre os dois atraves de um metodo
#--- separa os metodos em outro aquivo


from arquivoexerciciometodos import soma
from arquivoexerciciometodos import subt
from arquivoexerciciometodos import mult
from arquivoexerciciometodos import div_int
from arquivoexerciciometodos import div_frac
from arquivoexerciciometodos import resto
from arquivoexerciciometodos import raiz

n1= int(input('Digite um numero inteiro: '))
n2= int(input('Digite outro numero inteiro: '))

print(f'A soma é: {soma(n1,n2)}\nA Subtração é: {subt(n1,n2)} \nA Multiplicação é: {mult(n1,n2)} \nA Divisão Inteira é: {div_int(n1,n2)} \nA Divisão Fracionada é: {div_frac(n1,n2)} \nO Resto é: {resto(n1,n2)} \nA Raiz é: {raiz(n1,n2)}')


'''sub = num1 - num2
div = num1 / num2
multi = num1 * num2'''




