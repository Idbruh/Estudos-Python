# Aula 17 - 02-12-2019
# Funções, While, reforço de lista, tupla, dicionário


from bbb_2 import *


op = 0
while op != 7:
    print("#"*40)
    print('      H B S I S  -  Airlines')
    print("#"*40)
    print('   -- Controle de Acesso --\n ')
    print('\n1. Cadastro de embarque no Veículo\n2. Cadastro de embarque no Terminal\n3. Cadastro de embarque no Avião\n4. Relatórios\n\n7. Sair\n')
    print("#"*40)
    print(' \n')
    op = int(input('Opção: '))

    if op == 1:                                     # Cadastro VIAGENS CARRO
        
        print('''
-------------------------------------------------------        
C A D A S T R O   D E   E M B A R Q U E : FORTWO
-------------------------------------------------------

- Motorista do Carro informe o elemento de identificação:

Policial
Piloto
Chefe de Serviço

- Passageiro do Carro informe o elemento de identificação:

Oficial
Comissária de bordo
Presidiario

''')
        motorista = input('motorista: ')
        passageiro = input('passageiro: ')
        horario_partida = input('horario de partida  no formato hh:mm : ')
        previsao_chegada = input('horario da previsão de chegada (Viagem leva 10 minutos) no formato hh:mm : ')
        viagem_carro(motorista, passageiro, horario_partida, previsao_chegada)    
        ##Chamando a função >

                                # Ver viagens de carro cadastradas
        lista_viagensC = ler_viagensC()
        print('\nDetalhes Da Viagem')
        for linha in lista_viagensC:
            print(f"\nMotorista: {linha['Motorista']}\nPassageiro:{linha['Passageiro']}\nHorario Partida:{linha['Horario de Partida']}\nPrevisão de chegada: {linha['Previsão de Chegada']}\n")
    
    elif op == 2:
        print('''
-------------------------------------------------------
C A D A S T R O   D E   E M B A R Q U E  : TERMINAL
-------------------------------------------------------

Informe o elemento de identificação:

Policial
Piloto
Chefe de Serviço
Oficial
Comissária de bordo
Presidiario

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

    elif op == 3:                                   # Venda de produtos
        print('''
-------------------------------------------------------
C A D A S T R O   D E   E M B A R Q U E  : Avião
-------------------------------------------------------
Informe o elemento de identificação:

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
        print("="*40)
        print('    Detalhes Da Viagem FORTWO')
        print("="*40)
        for linha in lista_viagensC:
            print(f"\nMotorista: {linha['Motorista']}\nPassageiro:{linha['Passageiro']}\nHorario Partida:{linha['Horario de Partida']}\nPrevisão de chegada: {linha['Previsão de Chegada']}\n\n")

        lista_pessoasT = ler_pessoas_terminal()
        print("="*40)
        print('    Pessoas no Terminal')
        print("="*40)
        for linha in lista_pessoasT:
            print(f"\nElemento de Identificação: {linha['Elemento de Identificação']}\nNome:{linha['Nome Pessoa']}\n\n")

        
        lista_pesssoasA = ler_pessoas_aviao()
        print("="*40)
        print('    Pessoas no Avião')
        print("="*40)
        for linha in lista_pesssoasA:
            print(f"\nElemento de Identificação:{linha['elemento_id']}\nNome:{linha['nome_pessoa']}\n\n\n")

    elif op == 7:
        print('Obrigado volte sempre!')
    else:
        print('Opção invalida, tente novamente!')
        break