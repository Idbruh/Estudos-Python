# aula 4_2 - Booleanas

#---variavel booleana simples com True Ou False
validador = False
validador = True
#---- Criação de variável booleana atraves de expressão
print('='*50)
idade = 18
validador = (idade == 18)
print(validador)

if validador:
    print('maior')
print('='*50)
#----------- Criação de variavel booleana atraves de expressão de diferença
validador = (idade != 18)
print(validador)
#----------- Criação de variavel booleana atraves de expressão de maior
validador = (idade > 18)
print(validador)
#----------- Criação de variavel booleana atraves de expressão de menor
validador = (idade < 18)
print(validador)
#----------- Criação de variavel booleana atraves de expressão de  maior igual
validador = (idade >= 18)
print(validador)
#----------- Criação de variavel booleana atraves de expressão de menor igual
validador = (idade <= 18)
print(validador)
print('='*50)
#---expressão de negação : invertendo a expressão: if false ela vira true // if true ela vira false
validador = not True
validador = not False
#----------- Criação de variavel booleana atraves de expressão de 
validador1 = (idade>18 and idade<18) #---no caso do AND as duas precisam ser verdadeiras
validador1 = (idade<18 or idade==18) #---- valida se uma das duas condições são verdadeiras
print(validador1)

sorteado = 'Marcela'
validador2 = (sorteado=='Mateus'and sorteado=='Marcela')
print(validador2)

print('='*50)