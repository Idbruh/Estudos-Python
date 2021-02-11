# testes em sucuri

#verificação se determinada condição é verdadeira

assert True
assert (10==10)
assert (10>5)
assert ('Voltolini' != 'Vinicius')

def soma(n1,n2):
    resultado = n1+n2
    return resultado

def multiplicacao(n1, n2, n3=1):
    return n1 * n2 * n3

def checa_maioridade(idade):
    if idade >= 18:
        return True
    else:
        return False

assert soma(5,10) == 15
assert multiplicacao(2,4,6) == 48
assert multiplicacao(2,4) == 8

assert checa_maioridade(18) == True
assert checa_maioridade(19) == True
assert checa_maioridade(17) == False
