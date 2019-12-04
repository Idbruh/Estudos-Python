# Aula 19 - 04-12-2019
# Lista com for e metodos

# 1 - Com a seguinte lista imprima na tela (unsado a indexação e f-string) 

cadastroHBSIS = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                ]

# idade Carlos é 15 anos
# email de Mateus é d@d.com
print(f'A idade de {cadastroHBSIS[1][4]} é {cadastroHBSIS[3][4]} ')

# 2 - usando o for, imprima todos nomes um abaixo do outro
'''for i in cadastroHBSIS:
    lista = cadastroHBSIS[1][i]
    print(f'{cadastroHBSIS[0]}')'''
# nome  Alex telefone: 4799991
#
# 3 - Usando a indexação faça uma lista com 3 bibliotecas contendo os dados do Mateus, Paulo e João
#  contendo como chaves: nome, email, idade, telefone (nesta  sequencia)