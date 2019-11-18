#--- Exercicio 3  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia os dados de um funcionário
#--- Funcionário: Nome Completo, CPF, Número do registro, Cargo e Salário
#--- Exiba os dados de salário liquido, descontando os tributos
#--- Deve ser calculado o valor do INSS -
#--- INSS -  de    0,00 ate 1751,81 - percetual =  8,0%
#---         de 1751,82 ate 2919,72 - percetual =  9,5%
#---         de 2919,72 ate 5839,45 - percetual = 11,0%
#--- Deve ser calculado o valor do IRRF - 
#--- IRRF -  de    0,00 ate 1903,98 - percetual =  0,0%
#---         de 1903,98 ate 2826,65 - percetual =  7,5%
#---         de 2826,66 ate 3751,05 - percetual = 15,0%
#---         de 3751,06 ate 4664,68 - percetual = 22,5%
#---         de 4664,69 ate ------- - percetual = 27,5%
#--- Base - http://www.calculador.com.br/calculo/salario-liquido

nome = input('Digite o seu nome completo: ')
cpf = int(input('Digite o seu CPF: '))
nreg = int(input('Digite o número de sual matricula: '))
cargo = input('Digite se cargo: ')
salario = float(input('Digite o seu salário: $ '))

if salario <= 1751.81:
    print('O desconto do INSS é: $ ', salario*0.08)
elif salario <= 2919.72:
    print('O desconto do INSS é: $ ', salario*0.95)
else:
    print('O desconto do INSS é: $ ', salario*0.11)

if salario <= 1903.98:
    print('Você não tem desconto de IRRF.')
elif salario <= 2826.65:
    print('O desconto do IRRF é: $ ', salario*0.75)
elif salario <= 3751.05:
    print('O desconto do IRRF é: $ ', salario*0.15)
elif salario <= 4664.68:
    print('O desconto do IRRF é: $ ', salario*0.225)
else:
    print('O desconto do IRRF é: $ ', salario*0.275)
