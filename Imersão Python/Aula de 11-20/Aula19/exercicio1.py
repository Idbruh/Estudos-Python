# Aula 19 - 04-12-2019
# Lista com for e metodos

# 1 - Com a seguinte lista imprima na tela (unsado a indexação e f-string) 

cadastroHBSIS = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                ]

'''
# nome  Alex telefone: 4799991
print(f'\nnome {cadastroHBSIS[1][0]}  telefone {cadastroHBSIS[3][0]}')
# idade Carlos é 15 anos
print(f'A idade de {cadastroHBSIS[1][4]} é {cadastroHBSIS[7][4]}')
# email de Mateus é d@d.com
print(f'o email de {cadastroHBSIS[1][3]} é {cadastroHBSIS[5][3]}\n')


# 2 - usando o for, imprima todos nomes um abaixo do outro

for nomes in cadastroHBSIS[1]:
    print(f'{nomes}')'''

# 3 - Usando a indexação faça uma lista com 3 dicionários contendo os dados 
# do Mateus, Paulo # e João contendo
# como chaves: nome, email, idade, telefone (nesta  sequencia)


dados = [{cadastroHBSIS[0]}, {cadastroHBSIS[1][3]},{cadastroHBSIS[4]}, {cadastroHBSIS[5][3]}, {cadastroHBSIS[6]}, {cadastroHBSIS[7][3]}, {cadastroHBSIS[2]}, {cadastroHBSIS[3][3]},
        {cadastroHBSIS[0]}, {cadastroHBSIS[1][1]},{cadastroHBSIS[4]}, {cadastroHBSIS[5][1]}, {cadastroHBSIS[6]}, {cadastroHBSIS[7][1]}, {cadastroHBSIS[2]}, {cadastroHBSIS[3][1]},
        {cadastroHBSIS[0]}, {cadastroHBSIS[1][5]},{cadastroHBSIS[4]}, {cadastroHBSIS[5][5]}, {cadastroHBSIS[6]}, {cadastroHBSIS[7][5]}, {cadastroHBSIS[2]}, {cadastroHBSIS[3][5]},
        {cadastroHBSIS[0]}, {cadastroHBSIS[5][3]},{cadastroHBSIS[4]}, {cadastroHBSIS[5][4]}, {cadastroHBSIS[6]}, {cadastroHBSIS[7][4]}, {cadastroHBSIS[2]}, {cadastroHBSIS[3][4]},
        ]

print(dados)

