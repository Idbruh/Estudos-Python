# #-- revisão das aulas


# #-- for
# '''
# n_inicial = int(input('Qual numero você iniciar a soma? '))
# n_final = int(input('Agora até qual numero devemos somar? '))
# total = 0
# for numero in range(n_inicial,n_final+1):
#     # total = total + numero
#     total += numero
# print(f'total:{total}')'''

# '''
# total = 0
# for numero in [50,51,52,53,54,55,56,57] + list(range(58,101)):
#     # total = total + numero
#     total += numero

# print(f'total gohorse: {total}')'''

# #-- while

# texto = 'Tenho saudade do prof Abio. Python é legal. Bruno.'
# texto2 = "Tá legal, nosso proprio split, 3 textos em uma lista"
# print(texto.split('.'))

# def nosso_split(txt,sep):
#     #return txt.split(sep)
#     #first char
#     result = []
#     count = 0
#     ultimo_sep_posicao = 0
#     for char in txt:
#         if char == sep:
#             result.append(   txt[ultimo_sep_posicao:count]  )
#             ultimo_sep_posicao = count +1
#         count += 1
#     return result


# print(nosso_split(texto2,','))

# print('in range')
# for i in range(1,100,2)
#     print(i)

# print('in lista')
# for i in [1,2,3,4,5,6,7,8,9]:
#     print(i)

# print('in texto')
# for i in "Texto":
#     print(i)

# arquivo = open('arquivo.txt')
# soma = 0
# #interest = 'Lorem'  uinteresse literal
# interest = input('Digite a palavra que deseja contar: ') #interesse dinamico, perguntando para o usuário
# total_interest = 0
# for linha in arquivo:
#     print('Caracteres na linha: ', len(linha))
#     soma += len(linha)
#     total_interest += linha.lower().count(interest.lower())#-- todos os caracteres estão em minusculo
# arquivo.close()

# print('Arquivo com', soma, 'caracteres')
# print('A palavra', interest, 'apareceu',total_interest)

print('_______________________________________________________________________________________')

# For para dicionario

dias_de_cada_mes = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,

}


# print('O mês', qual_mes, 'tem', dias_de_cada_mes[qual_mes], 'dias')




# qual_mes = int(input('Digite aqui o mes que você quer: '))
# ate_o_final = 365 - dias_de_cada_mes[qual_mes] - dias_de_cada_mes[12 - qual_mes]

# print(f'O mês tem {qual_mes}')

# qual_mes = int(input('Digite aqui o mes que você quer: '))
# print(sum(list(dias_de_cada_mes.values())[qual_mes-1:]))
# print('Dias que faltam para acabar o ano, a partir do mes selecionado: ')

# print('_______________________________________________________________________________________')

# qual_mes = int(input('Digite aqui o mes que você quer: '))
# total = 0
# for mes in range(qual_mes,12+1):
#     total += dias_de_cada_mes[mes]
# print('modo estruturado')
# print('total de dias até o final do ano'. total)



# #for dicionario
# for chave in dias_de_cada_mes:
#     print('Tenho uma chave nessa linha', chave)
#     print('Tenho uma chave nessa linha', dias_de_cada_mes[chave])
# print('_______________________________________________________________________________________')

# for chave, valor in dias_de_cada_mes.items():
#     print('Para a chave', chave, 'o valor', valor)



#for tupla

tupla = ('Texto', 42, 5.01, int, str, list)

for isto in tupla:
    print(type(isto))



