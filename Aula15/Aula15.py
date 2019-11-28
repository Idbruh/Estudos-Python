#-- Módulo 15 - 28-11-2019
#-- Manipulação de arquivos
#-- dar o nome ao metodo "aula15.txt" | 'x' = abrir criar arquivo e abre para escrita | 'w' - escreve
#-- abrir paramentro e salvar na variavel 'arquivo'
#-- função write = escrever algo no arquivo

'''arquivo = open('aula15.txt','a')
arquivo.write('Voltolini\n')
arquivo.close()'''

arquivo = open('aula15.txt', 'r')
for linha in arquivo:
    print(linha)
arquivo.close()