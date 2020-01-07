# Aula 17 - 02-12-2019
# Funções, While, reforço de lista, tupla, dicionário


from def_ex1 import *


op = 0
while op != 7:
    print('''


############################################################### 
--------------------------------------------------------------  
            |  H B S I S  -  Airlines  | 
--------------------------------------------------------------
              -- Controle de Acesso --
###############################################################
1. Cadastro de embarque no Veículo
2. Cadastro de embarque no Terminal
3. Cadastro de embarque no Avião
4. Relatórios
--------------------------------------------------------------
7. Sair
###############################################################

''')
    op = int(input('Opção: '))

    if op == 1:                                     # Cadastro VIAGENS CARRO
        
        print('''
###############################################################
            |  H B S I S  -  Airlines  | 
--------------------------------------------------------------        
C A D A S T R O   D E   E M B A R Q U E : FORTWO
--------------------------------------------------------------
###############################################################
-------------------------------------------------------------- 
Informe o elemento de identificação do motorista do carro:
 

policial
piloto
chefe de servico

-------------------------------------------------------------- 

Informe o elemento de identificação do passageiro do carro:
 

oficial
comissaria
presidiário
###############################################################
''')    

        motorista = input('motorista: ')
        passageiro = input('passageiro: ')
       
        while motorista != 'policial' and motorista != 'piloto' and motorista != 'chefe de servico':
            print('Para esta operação, apenas são aceitos como motorista: policial, piloto ou chefe de servico')
            print('Por favor, digite novamente o motorista')
            motorista = input('motorista: ')
            # while not tem_presidiario_com_policial(motorista, passageiro):
            #     print('Um presidiário não pode viajar sem um policial')
            #     print('Por favor, digite novamente o passageiro')
            #     passageiro = input(passageiro)

        if motorista != 'policial' and passageiro == 'presidiário':
            print('Um presidiário não pode viajar sem um policial.\n')
            print('Por favor, digite novamente o elemento de identificação do passageiro: ')
            passageiro = input('passageiro: ')

        elif motorista == 'piloto' and passageiro != 'chefe de servico' and passageiro != 'policial' and passageiro != 'oficial':
            print('Este motorista não pode levar esse passageiro.\n')
            print('Por favor, digite novamente o passageiro: ')
            passageiro = input('passageiro: ')

        elif motorista == 'chefe de servico' and passageiro != 'piloto' and passageiro != 'policial' and passageiro != 'comissaria':
            print('Este motorista não pode levar esse passageiro.\n')
            print('Por favor, digite novamente o elemento de identificação do passageiro: ')
            passageiro = input('passageiro: ')

        elif motorista == 'policial' and passageiro != 'chefe de servico' and passageiro != 'piloto' and passageiro != 'presidiario':
            print('Este motorista não pode levar esse passageiro')
            print('Por favor, digite novamente o elemento de identificação do passageiro: ')
            passageiro = input('passageiro: ')
        else:
            pass
            # print('Um presidiário não pode viajar sem um policial')
            # print('Por favor, digite novamente o passageiro')
            # passageiro = input(passageiro)
            

        
        horario_partida = input('horario de partida  no formato hh:mm : ')
        previsao_chegada = input('horario da previsão de chegada (Viagem leva 10 minutos) no formato hh:mm : ')
        viagem_carro(motorista, passageiro, horario_partida, previsao_chegada)    
    

                                # Ver viagens de carro cadastradas
        lista_viagensC = ler_viagensC()
        print('\nDetalhes Da Viagem')
        for linha in lista_viagensC:
            print(f"\nMotorista: {linha['Motorista']}\nPassageiro:{linha['Passageiro']}\nHorario Partida:{linha['Horario de Partida']}\nPrevisão de chegada: {linha['Previsão de Chegada']}\n")
    
    elif op == 2:
        print('''
###############################################################
            |  H B S I S  -  Airlines  | 
--------------------------------------------------------------   
C A D A S T R O   D E   E M B A R Q U E  : TERMINAL
--------------------------------------------------------------
###############################################################
---------------------------------------------------------------
Informe o elemento de identificação:


policial
piloto
chefe de servico
oficial
comissaria
presidiario

###############################################################
''')                                   
# Cadastro de pessoas no terminal
        elemento_id = input('Informe o elemento de identificação: ')
        nome_pessoa =  input('Informe o seu Nome: ')
        salvar_pessoas_terminal(elemento_id, nome_pessoa)
        
                                    # Ver Pessoas no terminal
        lista_pessoasT = ler_pessoas_terminal()
        print('Pessoas no Terminal:')
        for linha in lista_pessoasT:
            print(f"\nElemento de Identificação: {linha['Elemento de Identificação']}\nNome:{linha['Nome Pessoa']}\n")

    elif op == 3:                                   # C A D A S T R O   D E   E M B A R Q U E aviao
        
        print('''
###############################################################
            |  H B S I S  -  Airlines  | 
--------------------------------------------------------------   
 C A D A S T R O   D E   E M B A R Q U E  : Avião
---------------------------------------------------------------
###############################################################
---------------------------------------------------------------
Informe o elemento de identificação:
---------------------------------------------------------------
Policial
Piloto
Chefe de Serviço
Oficial
Comissária de bordo
Presidiario

''')                                   # Cadastro de pessoas no terminal
        
        elemento_id = input('Informe o elemento de identificação: ')
        nome_pessoa = input('Informe o seu Nome: ') 
        salvar_pessoas_aviao(elemento_id, nome_pessoa)   

        lista_pesssoasA = ler_pessoas_aviao()
        print('\nPessoas no Avião:\n')
        for linha in lista_pesssoasA:
            print(f"Elemento de Identificação:{linha['elemento_id']}\nNome:{linha['nome_pessoa']}\n")
    elif op == 4:
        lista_viagensC = ler_viagensC()
        print('''
###############################################################
            |  H B S I S  -  Airlines  | 
--------------------------------------------------------------   
            RELATORIO DE VIAGENS : FORTWO
---------------------------------------------------------------
###############################################################
''')
        for linha in lista_viagensC:
            print(f'''
Motorista: {linha['Motorista']}
Passageiro:{linha['Passageiro']}
Horario Partida:{linha['Horario de Partida']}
Previsão de chegada: {linha['Previsão de Chegada']}
---------------------------------------------------------------
''')

        lista_pessoasT = ler_pessoas_terminal()
        print('''
###############################################################
            |  H B S I S  -  Airlines  | 
--------------------------------------------------------------   
         RELATORIO DE PESSOAS NO TERMINAL
---------------------------------------------------------------
''')
        for linha in lista_pessoasT:
            print(f'''
Elemento de Identificação: {linha['Elemento de Identificação']}
Nome:{linha['Nome Pessoa']}

---------------------------------------------------------------
''')

        lista_pesssoasA = ler_pessoas_aviao()
        print('''
###############################################################
            |  H B S I S  -  Airlines  | 
--------------------------------------------------------------   
            RELATORIO DE PESSOAS NO AVIÃO
---------------------------------------------------------------
###############################################################

''')
        for linha in lista_pesssoasA:
            print(f'''
Elemento de Identificação:{linha['elemento_id']}
Nome:{linha['nome_pessoa']}

---------------------------------------------------------------
''')

    elif op == 7:
        print('Obrigado volte sempre!')
    else:
        print('Opção invalida, tente novamente!')
        break