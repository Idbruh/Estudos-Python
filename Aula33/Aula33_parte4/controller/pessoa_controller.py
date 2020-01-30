import sys
sys.path.append('/Users/900133/Documents/GitHub/TrabalhosPyhton/Aula33/Aula33_parte4')
from model.pessoa import Pessoa
from Dao.pessoadb import PessoaDb

class PessoaController:
    p = Pessoa()
    p_db = PessoaDb()

    def listar_todos(self):
        return self.p_db.listar_todos()

    def exportar(self):
        lpc = self.p_db.listar_todos()
        self.p.exportar_txt(lpc)