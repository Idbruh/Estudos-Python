#Crie um programa que leia 4 notas ok
#Imprima a maior nota ok
#Imprima a menor nota
#Imprima a media
#imprima se o aluno foi aprovado ou reprovado(média 7.0)

#Crie um programa que leia 4 notas ok

print('=' * 50) 
Aluno = input('digite o nome do aluno: ')
print('=' * 50)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

#Imprima a maior nota
''' lista = [nota1, nota2, nota3, nota 4]
    print ('A maior nota foi:', max(lista))'''

print('=' * 50)
if nota1 > nota2 and nota1 > nota3 and nota1 > nota4:
    print ('a maior nota é a primeira: ', nota1)
elif nota2 > nota3 and nota2 > nota4:
    print ('a maior nota é a segunda: ', nota2)
elif nota3 > nota4:
    print ('a maior é a terceira:', nota3)
else:
    print ('a maior é a quarta nota:', nota4)
print('=' * 50) 
#Imprima a menor nota
''' lista = [nota1, nota2, nota3, nota 4]
    print ('A menor nota foi:', min(lista))'''

if nota1 < nota2 and nota1 < nota3 and nota1 < nota4:
    print ('a menor nota é a primeira: ', nota1)
elif nota2 < nota3 and nota2 > nota4:
    print ('a menor nota é a segunda: ', nota2)
elif nota3 < nota4:
    print ('a menor é a terceira: ', nota3)
else:
    print ('a menor é a quarta nota: ', nota4)
print('=' * 50) 

# média
media = ((nota1 + nota2 + nota3 + nota4) / 4 )
print (f'A média é: {media} ')
print('=' * 50) 

#imprima se o aluno foi aprovado ou reprovado(média 7.0)
if media >= 7.0:
    print(f'{Aluno}: Aprovado!')
else:
    print(f'{Aluno}: Reprovado!')
print('=' * 50) 

