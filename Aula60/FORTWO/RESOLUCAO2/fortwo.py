
class Fortwo:
    def __init__(self):
        self.__pessoas_permitidas = ['piloto', 'chefe de serviço','policial']
        self.__motorista = ''
        self.__passageiro = ''

    def set_motorista(self, pessoa):
        if pessoa in self.__pessoas_permitidas:
            self.__motorista = pessoa

    def get_motorista(self):
        return self.__motorista

    def set_passageiro(self, pessoa):
       if self.__valida_regra_passageiro__(pessoa):
            self.__passageiro = pessoa

    def __valida_regra_passageiro__(self, pessoa) -> bool:
        if self.__motorista == 'policial':
            if pessoa == 'presidiario':
                return True
        elif self.__motorista == 'piloto':
            if pessoa != 'comissário1' and pessoa != 'comissário2' and pessoa != 'presidiario':
                return True
        elif self.__motorista == 'chefe de serviço' :
            if pessoa != 'oficial1' and pessoa != 'oficial2' and pessoa != 'presidiario':
                return True
        return False

    def get_passageiro(self):
        return self.__passageiro