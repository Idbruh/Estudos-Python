'''classe: ela passa argumentos e recebe parametros
retorna uma variavel em formato de tupla

atributos são variaveis que pertencem a classe'''

#----- Metodos
#-- Parametros ordenados: passa argumentos na ordem


def soma(n1,n2):
    resultado = n1+n2
    return resultado

res = soma(10,20)
print(res)

#-- Parametros nomeados: tem que nomear todos os argumentos

def subtracao(n1,n2,n3):
    resultado = n1-n2-n3
    return resultado


res2 = subtracao(n3 =10,n2=20,n1=10)
print(res2)

#-- Parametros opcional: passa um valor padrão(default), no qual n fará diferença

def multiplicacao(n1,n2,n3=1):
    return n1+n2+n3

res3 = multiplicacao(10,20,30)
print(res3)


#----- Classe --- tudo o que tem n classe pode ser acessado como objeto
#instanciando um objeto de classe Calc

#quando se quer acessar algo de fora da classe, deve passar como parametro
#e quando quer usar algo que está dentro passa com self. na frente
#variavel privada = __resultado que não deve ser acessado de fora
#metodo init: ou metodo construtor

class Calc:
    n1 = 0
    n2 = 0
    resultado = 0

    def __init__(self, numero1, numero2):
        self.n1 = numero1
        self.n2 = numero2

    def soma(self):
        self.resultado = self.n1 + self.n2

    def subtracao(self):
        resultado = self.n1 - self.n2
        return resultado

    def multiplicacao(self):
        resultado = self.n1 * self.n2 + self.n3
        return resultado
c = Calc(10,20)                         # sem parentesis ele é só uma classe, n um objeto...
resu = c.soma(10,20)               # para usar o resultado depois tem q armazenar em uma variavel, já que n está salva em um espaço da memoria
print(resu)