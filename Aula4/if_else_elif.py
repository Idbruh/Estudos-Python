#aula 4 11-11-2019
#estrutura de decisão
#if valida se é true
idade = 17.5
#-------- if simples, validação apenas uma condição
if idade == 18:
    print( 'maior')

#-------- if + else: caso a condição validada pelo IF seja 'não verdadeira', o ELSE é executado
if idade < 18:
    print('menor')
else:
    print(' maior')

#--------   IF com ELIF e ELSE: caso a condição validada no IF seja falsa, a condição ELIF será validado e caso seja falsa, o ELSE é executado

if (idade <18):
    print('dimenor')
elif idade == 18:
    print('silasco')
else:
    print('silascoMaisAinda')

#--- IF com variável booleana
'''em casod e  variavel booleana, não e necessário a validação(==true), pois o IF já valida se o conteúdo é TRUE, senão vai para o 
Else'''

ativo = True
if ativo:
    print('logar')
else:
    print('não logar')