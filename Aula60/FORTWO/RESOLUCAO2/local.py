
class Local:
    def __init__(self, lista:list):
        self.__pessoas = lista

    def entrada(self, pessoa:str):
        self.__pessoas.append(pessoa)

    def saida(self, pessoa:str):
        self.__pessoas.remove(pessoa)

    def __str__(self):
        lista_formatada = ''
        for p in self.__pessoas:
            lista_formatada = lista_formatada + f' {p} '
        return lista_formatada