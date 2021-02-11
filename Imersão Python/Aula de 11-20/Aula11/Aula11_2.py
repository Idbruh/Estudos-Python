# --- 2.Crie um procgrama que calcule a renabilidade anual de um investimento
#     baseando-se em sua rentabilidade deve ser apresentada em % e R$
#       --- Utilizar metodos

from metodos_exer import ren_investimento, calc_mes

v_inicial = float(input('Informe o valor investido inicialmente: $ '))
v_porcentagem = float(input('Informe a rentabilidade mensal: %  '))


print(f'Com R$ {v_inicial:.2f} investidos inicialmente, em um percentual de {v_porcentagem}, em 12 meses você terá: $ {ren_investimento(v_inicial,v_porcentagem):.2f}\n\nmensal')

'''M é o montante final obtido na aplicação, ou seja, o saldo após a aplicação do juros;
i é a taxa de juros aplicada, em porcentagem;
C é o capital ou valor inicial aplicado;
t é o tempo total da aplicação.'''