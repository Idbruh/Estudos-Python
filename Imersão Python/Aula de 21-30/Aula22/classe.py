#---1. O que a pessoa(classe) tem? Quais são as caracteristicas?
#--- resposta: 
# - Atributos: pode ser definida como variável
# nome
# idade
# telefone
# sexo 

#---2. O que uma pessoa faz?
# #--- resposta: 
# # - Está associada a métodos(função|procedimentos)-- podendo ter ou não return, ser somente um print ou passar via .self
# respira
# dorme
# corre
# bebe 
# come  
# multiplica ###

# #---3. Como a pessoa está agora?
# #--- resposta:
# # - Atributos de estado -  muda o estatus da 'pessoa'
# divida # compram e passa de n devedor para devedor
# casadada # pessoa deixa de estar descansada e passa a estar cansada
# viva
# fome
# sede  

#para criar uma classe deve passar os parametros depois.. e os parametros podem ou ner ter o mesmo nome
# que a variavel

# sempre começã com letra maiuscula

class Pessoa: 
    '''
    Esta classe é uma demonstração para aula
    '''
    
    #pass serve para deixar a classe em branco
    
    def __init__(self,nome1,idade1,telefone1,sexo1):
        ''' 
        O '__init__' é  o motor que irá iniciar as variavéis da classe
        O 'self' é o que irá conectar toda a classe
        '''
        # - caracteristicas para ser uma pessoa neste programa
        self.nome = nome1
        self.idade = idade1
        self.telefone = telefone1
        self.sexo = sexo1

        # - atributos de estado
        self.respira = True
        self.divida = None   #-- None: quando não se sabe o valor
        self.cansada = 'não'
        self.viva = True
        self.fome = 'sim' 
        self.sede = 'não'  

        # - Metodos
        
        def respira (self,respirar):
            if respirar == True: #- se ela respira
                self.viva = True #- então self.vida verdade
            else: #- senão
                self.viva = False #- falso
                
        def corre (self,distancia):# peessoa corre uma distancia somente se estiver viva
            if self.viva:
                if distancia >= 50 and distancia < 100:
                    self.cansada = 'pouco'
                    self.sede = 'pouco'
                    self.fome = 'pouco'
                elif distancia >= 100 and distancia < 200:
                    self.cansada = 'medio'
                    self.sede = 'medio'
                    self.fome = 'medio'
                elif distancia > 200:
                    self.cansada = 'muito'
                    self.sede = 'muito'
                    self.fome = 'muito'

        def dorme (self,dorme):
            if self.viva:
                self.cansada = 'não'
                self.come()
                self.bebe()
       
        
        def bebe (self,bebe):
            if self.viva:
                    self.sede = 'não'
    
        def come (self,come):
            if self.viva:
                self.fome = 'não'
        
        
p = Pessoa('Antonio',18,4199999999,'m')

p.respira(False)

p.corre(300)
p.dorme()
p.come()
p.bebe()

print(f'Nome é: {p.nome}')
print(f'Está vivo? {p.viva}')
print(f'Está com fome? {p.fome}')
print(f'Está com sede? {p.sede}')
print(f'Está cansado? {p.cansada}')
    
     




 