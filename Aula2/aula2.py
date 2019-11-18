idade = 27 #numero_inteiro
salario = 490.00 #numero_real
nome = 'idBruh' #string(palavras e frases): precisa estar entre as aspas 
verdadeiro = True
falso = False

print('=' * 50) 
print('\n' * 3) #pula para a proxima linha(\n) * 3
print('\t Testee', 'da', "aula2") #tab(\t): dar espaço maior
print('idade:', idade, 'salario:' ,salario, 'nome:', nome, 'verdadeiro:', verdadeiro,'falso:', falso)
print('idade:{} salario:{} nome:{}'.format(idade, salario, nome)) #formatar variavel: {}
print(f'idade:{idade} salario:{salario} nome:{nome}') #interpolação de string
print('\n'*3)
print('='*50)


print('''este FDS eu fui para a praia tomar sol
         e fiquei no sol fazendo exercicio de python
         e fiquei todo queimado''')

nome_completo = 'Bru ' '' 'Carmo'#--- concatenação de string
print(nome_completo)