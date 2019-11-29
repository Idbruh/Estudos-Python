#-- ler uma string do console (input('---'))
#-- armazenar em uma variaver
#-- ler no arquivo de texto

nome = (input('Digite o nome: '))

arquivo = open('exercicio1.txt','a')
arquivo.write(f'{nome}\n')
arquivo.close()


#-- O U T R A  F O R M A(porem não ideal): input  na variavel direto -- usar aspas duplas (independente se vai ser dentro
# ou fora da interpolação... necessário alterar para 'sub string' )

arquivo = open('exercicio1.txt','a')
arquivo.write(f"{input('Digite o nome: ')}\n")
arquivo.close()
