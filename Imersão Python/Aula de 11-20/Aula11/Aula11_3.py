# --- 3.Crie um programa para calculo de investimento 
# --- solicitar valor a ser investido no Tesouro Selic
# Calcular o valot total até o vencimento do titulo
#       --- Utilizar metodos


def tesouro_direto(v_inicial,v_porcentagem, periodo):
    montante =  (v_inicial * (1 + (v_porcentagem/100)) ** periodo)
    return montante    

v_inicial = float((input('Digite o valor do investimento: ')))
periodo = input('Digite o valor do periodo: '))
taxa = float(input('Digite o valor da taxa Selic: '))
valor_minimo = 104.1
taxa_tesouro =  0.02 + taxa


cotas = v_inicial//cotas
valor_investimento = cotas * valor_minimo







