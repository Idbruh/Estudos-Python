#estrutura de repetição FOR

'''
#-- for simples usando range com incremento padrão 1
for i in range(1,10):#range: define o intervalo de valores até 1-9(ultimo elemento não incluso)
    print(f'{i}-Padawans HbPY')
print('-'*50)
#----
for i in range(0,10):#range: define o intervalo de valores até 0-9 (inicia-se com 0)
    print(f'{i}-Padawans HbPY')
print('-'*50)
for i in range(0,10):#range "i+1': define o intervalo de valores até 1-10 (inicia-se com 0)
    print(f'{i+1}-Padawans HbPY')
print('-'*50)
for i in range(0,10,2):#range: define o intervalo de valores até 0-8 (inicia-se com 0) seleciona de 2 em 2
    print(f'{i}-Pares')
print('-'*50)
for i in range(0,10,2):#range: define o intervalo de valores até 0-10 
    print(f'{i+1}-impares')'''



lista = ['Mateus', 'Matheus','Marcela','Nicole','Tonho','Pablo']
'''for i in range(0,6):
    print(lista)'''

lista.append('Natan')
'''for sortudo in lista:
    print(sortudo)'''
#range 0 == 1-9
numero = 10
for i in range(0,10):
    print(f'{i} x {numero} = {i*numero}')
print('-'*50)
# range 0+1 == 1-10 
numero = 10
for i in range(0,10):
    print(f'{i+1} x {numero} = {i*numero}')
    #ou for i in range(0,11):
#    print(f'{i} x {numero} = {i*numero}')