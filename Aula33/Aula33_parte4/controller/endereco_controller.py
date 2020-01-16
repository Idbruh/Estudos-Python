import sys
sys.path.append('/Users/900133/Documents/GitHub/TrabalhosPyhton/Aula33/Aula33_parte4')
from model.endereco import Endereco
from dao.enderecodb import EnderecoDb

class EnderecoController:
    e = Endereco()
    e_db = EnderecoDb()

    def listar_todos(self):
        return self.e_db.listar_todos()

    def exportar(self):
        lpc = self.e_db.listar_todos()
        self.e.exportar_txt(lpc)