#-- 1. O programa deve ter um menu interativo com cabeçalho
#-- ver clientes cadastrados 
# 
#  



menu = '''
----------------------------------------------------------------------------------------------------
- 1. Cadastro de clientes                                                                          -
- 2. Ver clientes cadastrados                                                                      -
- 3. Cadastro de produtos                                                                          -
- 4. Ver produtos cadastrados                                                                      -
- 5. Vendas                                                                                        -
- 6. Relatórios de Vendas                                                                          -
----------------------------------------------------------------------------------------------------
- 7. Sair                                                                                          -
----------------------------------------------------------------------------------------------------


Digite a opção desejada: '''

while True:
    opcao = input(menu)
    if opcao == '1':
        print('Cadastro de clientes')
    elif opcao == '2':
        print('Ver clientes cadastrados')
    elif opcao == '3':
        print('Cadastro de produtos')
    elif opcao == '4':
        print('Ver produtos cadastrados')
    elif opcao == '5':
        print('Vendas')
    elif opcao == '6':
        print('Relatórios de Vendas')
    elif opcao == '7':
        print('Sair')
        break
    else:
        print('Valor inválido')



