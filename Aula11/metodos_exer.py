def valor_software(v_h,h_gastas,v_iss):
    return ((v_h*h_gastas)*(v_iss / 100))

################################################################################################

def ren_investimento(v_inicial,v_porcentagem):
    montante =  (v_inicial * (1 + (v_porcentagem/100)) ** 12)
    return montante    
# def calc_mes(v_inicial,v_porcentagem)
#     val_mes = v_inicial * v_porcentagem
#     return val_mes

################################################################################################


def tesouro_direto(v_inicial,v_porcentagem, periodo):
    montante =  (v_inicial * (1 + (v_porcentagem/100)) ** periodo)
    return montante    


def porcentagem_cotas()