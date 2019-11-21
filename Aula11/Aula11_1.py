# --- Aula 11 - 21-11-2019   
# --- 

# --- 1.Crie um programa que calcule
#     o imposto ISS de um serviço de desevolvimento de software
#       --- Utilizar metodos(valor base)
# --- 2.Crie um procgrama que calcule a renabilidade anual de um investimento
#     baseando-se em sua rentabilidade deve ser apresentada em % e R$
#       --- Utilizar metodos
# --- 3.Crie um programa para calculo de investimento
#       --- Utilizar metodos
# --- 4.
#       --- Utilizar metodos
# --- 5.


#--- E x e r c i c i o   1

from metodos_exer import valor_software

v_h = float(input('Quanto você cobra a sua hora: '))
h_gastas = int(input('Digite quantas horas você gastou: '))
v_iss = float(input("Digite o valor do ISS: %  "))



print(f'O valor do software, com imposto ISS de {v_iss} calculado, será: $ {valor_software(v_h,h_gastas,v_iss):.2f}')
