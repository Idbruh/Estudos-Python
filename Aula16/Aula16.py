# Aula 16 29-11-2019
# ???????????(segredo)
# ver arquivo "faixa.py"
#criar, salvar e ler uma cadastro de playlist

from faixa import criar_faixa,salvar_faixa,ler_faixa


# Cadastro de playlist
# lendo musica, artista e album
musica = input('Digite o nome da musica: ')
album = input('Digite o nome do album: ')
artista = input('Digite o nome dx artista: ')

faixa1 = criar_faixa(musica, album, artista)
salvar_faixa(faixa1)

lista = ler_faixa()
#-- f de faixa
for f in lista:
    print(f"{f['musica']} - {f['artista']} - {f['album']}")


#-- primeiro pede as informações necessárias ''x  = input('Digite a informação x: ')''
#-- para armazenar os dados crie dicionarios(para as informações façam sentidos juntas)
#-- criar uma variavel para arazenar o dicionário: 
# entre {'musica': musica<-- variavel} separa por ','
# -- criar um metodo ( def criar_faixa(): ) 
# # pedindo o retorno do dicionario (retrn tem que ser a ultima linha)
#  -- chama o metodo com parametros das variaveis de fora do metodo
# import do arquivo que os metodos foram criados-- chamando pela função
#variavel faixa do método é diferente da variavel nomeada tbm de
# faixa no código são diferentes 
# armazenar 'open('nome.txt','a'-- abre como 'a'--)'
# em uma variavel == arquivo
# -- separa com a formatação e chama o dicionario(faixa) que foi 
# criado do metodo no outro arquivo(f"{faixa['musica']};{};{}")
#fecha o arquivo usando .close()
#-- cria  metodo (salvar função) para importar separa com virgula
# e digita ctrl + espaço para saber se está tudo certo com o metodo 
#chama o metodo salvar_faixa, passando o paramentro (faixa, ou faixa1, faixa2...)
# variavel lista:: lista de didiconarios :: pode exibir como quiser
#  
# 
#  
# 
#  