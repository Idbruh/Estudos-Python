from geradorlista import lista_simples_int_str
from geradorlista import lista_simples_inpura_int_str
from geradorlista import lista_simples_int
from geradorlista import lista_simples_str
from geradorlista import lista_simples_impura
from geradorlista import embaralhar
from geradorlista import embaralhar_int_str_hard
from geradorlista import binario

lista_nome = []
def nomes():
    posicao = 1
    quant = 5
    for i in range(quant):
        nome = input(f'Digite a {posicao} pessoa: ')
        lista_nome.append(nome)
        posicao += 1
    return(nomes)
    

print(nomes)
