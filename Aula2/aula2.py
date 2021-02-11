idade = 27 #numero_inteiro
salario = 490.00 #numero_real
nome = 'Idbruh_1' #string(palavras e frases): precisa estar entre as aspas 
verdadeiro = True
falso = False
print('-----------------')
print('=' * 50) 
print('\n' * 3) #pula para a proxima linha(\n) * 3
print('\t Testee', 'da', "aula2") #tab(\t): dar espaço maior
print('idade:', idade, 'salario:' ,salario, 'nome:', nome, 'verdadeiro:', verdadeiro,'falso:', falso)
print('idade:{} salario:{} nome:{}'.format(idade, salario, nome)) #formatar variavel: {}
print(f'idade:{idade} salario:{salario} nome:{nome}') #interpolação de string
print('\n'*3)
print('='*50)

print('='*50)
print('''este FDS eu fui para a praia tomar sol
         e fiquei no sol fazendo exercicio de python 
         e fiquei todo queimado''')

print('='*50)

print('='*50)
nome_completo = '  bru ' '' 'Carmo '#--- concatenação de string
print(nome_completo)

print((nome_completo).count('a'))
print((nome_completo).lower()) #--- .lower: tudo minusculo
print((nome_completo).upper())#--- .upper: tudo maiusculo
print((nome_completo).split(' ') )
print((nome_completo).strip().split('a') )
print((nome_completo).strip() )#--- .remover os espaços em  branco - começo e fim // remove formataçao e tabulação
print((nome_completo).strip() )
print((nome_completo).capitalize() )#--- .capitalize: primeira letra em maiusculo'''

print('='*50)

print('='*50)
pessoa = [" ","Exemplo1","Exemplo2","Exemplo3"]
print(pessoa)
print((' olha ').join(pessoa))
frase = 'cinquenta.'
print('a'.join(frase))
print(pessoa[1:])# : == onde começa e onde termina
print(pessoa[1:3])#espaço tambem conta
print(pessoa[:2])
print(pessoa[1], pessoa[2])
print(frase[5:])
print(frase[:4])
print(frase[5:10])
print(pessoa.count("Exemplo1"))#verificar se uma palavra existe na lista string tem que estar correto
print(pessoa.count("exemplo1".strip().capitalize()))

