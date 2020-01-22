import sys
sys.path.append('/Users/900133/Documents/GitHub/TrabalhosPyhton/Aula37')
from Dao.squad_dao import SquadDao
from Model.squad import Squad


class SquadController:
    dao = SquadDao()


    def listar_todos(self):
        lista_squad = []
        lista_tuplas = self.dao.listar_todos()
        for s in lista_tuplas:
            squad = Squad()
            squad.id =  s[0]
            squad.nome = s[1]
            squad.descricao = s[2]
            squad.numeropessoas = s[3]
            squad.linguagembackend = s[4]
            squad.frameworkfrontend = s[5]
            
            lista_squad.append(squad)
        return lista_squad

    def buscar_por_id(self, id):
        s = self.dao.buscar_por_id(id)
        squad = Squad()
        squad.id =  s[0]
        squad.nome = s[1]
        squad.descricao = s[2]
        squad.numeropessoas = s[3]
        squad.linguagembackend = s[4]
        squad.frameworkfrontend = s[5]
        return squad

    def salvar(self, squad:Squad):
        return self.dao.salvar(squad)

    def alterar(self, squad:Squad):
        self.dao.alterar(squad)

    def deletar(self, id):
        self.dao.deletar(id)

