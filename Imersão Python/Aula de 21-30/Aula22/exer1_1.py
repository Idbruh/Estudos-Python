# Aula 21 - 09-12-2019

# Crie uma classe cliente:

# 1) deve ter como atributos: codigo, cpf, nome, idade, sexo

# 2) como metodos: receber salario, comprar, pagar divida

# Quando recebe aumenta o dinheiro na carteira.

# quando compra aumenta os bens e diminui o dinheiro na carteira

# Se comprar e não tiver dinheiro o suficiente deve diminuir o dinheiro da carteira
# e aumentar a divida.

# Para pagar a divida tem que ter dinheiro o suficiente na carteira

# 3) atributos de estado: dinheiro na carteira, divida, bens


# - caracteristicas para ser uma pessoa neste programa
class Cliente:
        '''Esta classe contém informações sobre Clientes'''
# -caracteristicas para ser uma pessoa neste programa
        def __init__(self,nome1,idade1,sexo1,codigo1,cpf1):
                self.nome = nome1
                self.idade = idade1
                self.sexo = sexo1
                self.codigo = codigo1
                self.cpf = cpf1
        # - atributos de estado
                self.dinheiro_na_carteira = 0
                self.divida = 0
                self.bens = []
                # - Metodos receber salario, comprar, pagar divida

        def recebe (self,receber):
                #if self.dinheiro_na_carteira == 0:
                self.dinheiro_na_carteira = receber + self.dinheiro_na_carteira
        def compra (self,bem,valor):
                self.bens.append(bem)
                if valor <= self.dinheiro_na_carteira:
                        self.dinheiro_na_carteira = self.dinheiro_na_carteira - valor
                else:
                        self.divida = self.divida - (self.dinheiro_na_carteira - valor)
                        self.dinheiro_na_carteira = 0
        def divida (self,divida):
                if self.divida < self.dinheiro_na_carteira:
                        self.divida = self.bens - self.dinheiro_na_carteira
                


        
                        

cliente1 = Cliente('Bruna', 27, 'f', 10001, 18366333930)
cliente2 = Cliente('Aline', 15, 'f', 10002, 18366251930)

# receber = float(input('Digite o valor recebido: R$ '))
# comprar = float(input('Digite o valor da compra: R$ '))
# divida = comprar - receber



cliente1.recebe(300000)

cliente1.compra('casa',100000)

print(cliente1.dinheiro_na_carteira)
print(cliente1.bens)
print(cliente1.divida)