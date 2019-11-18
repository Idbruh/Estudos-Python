#--- Exercicio 5  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia o salário de uma pessoa
#--- Use o método 50-20-10-20 - https://www.jaseimevirar.com/blog/como-voce-organiza-seu-orcamento-mensal/
#---(50% gastos, 20% investimentos a longo prazo, 10% investimentos a curto prazo, 20% livre)
#--- Informe os percentuais e valores que a pessoa deve utilizar em cada categoria
#--- Deve ser utilizado a função format e os caracteres de tabulação e quebra de linha para cada categoria

nome = input('Digite o seu nome completo: ')
salario = float(input('Digite o seu salário: $ '))

gasto1 = salario*50/100
gasto2 = salario*20/100
gasto3 = salario*10/100
gasto4 = salario*20/100

print(f'\nOlá {nome}, seguem abaixo os valores para cada categoria: \n\nSalario total: {salario:.2f}\n\nContas fixas: {gasto1:.2f}\n\nInvestimentos de longo prazo: {gasto2:.2f}\n\nInvestimentos de curto prazo: {gasto3:.2f}\n\nGasto livre: {gasto4:.2f}\n')
