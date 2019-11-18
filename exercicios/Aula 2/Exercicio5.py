#--- Exercicio 5  - Variávies e impressão com interpolacão de string
#--- Imprima os dados de 5 papeis cotatos na bolsa de valors de SP
#--- Os dados dos papeis devem estar em variáveis
#--- Papel: Nome, Tipo, Cotação Atual e Valores Min e Max do dia 
#--- A tela deve conter cabeçalho e rodapé 

print('--'*40)

cabecalho = ('I B O V E S P A    17/11/2019')
papel1 = ('AMBEV - ABEV3\nTipo: Ordinária\nValor Minimo: $ 17,31\nValor Maximo: $ 17,61')
papel2 = ('PETROBRÁS - PETR3\nTipo: Ordinária\nValor Minimo: $ 31,59\nValor Maximo: $ 32,51')
papel3 = ('ELETROBRAS - ELET3 \nTipo: Ordinária\nValor Minimo: $ 35,69\nValor Maximo: $ 36,66')
papel4 = ('Cia Vale Rio Doce - VALE3\nTipo: Ordinária\nValor Minimo: $ 47,00\nValor Maximo: $ 47,58')
papel5 = ('CIELO SA - CIEL3\nTipo: Ordinária\nValor Minimo: $ 7,88\nValor Maximo: $ 8,19')
print(f'\n{cabecalho}\n\nFolha 1: {papel1}\n\nFolha 2: {papel2}\n\nFolha 3: {papel3}\n\nFolha 4: {papel4}\n\nFolha 5: {papel5}\n')

print('--'*40)