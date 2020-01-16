import sys
sys.path.append('/Users/900133/Documents/GitHub/TrabalhosPyhton/Aula33/Aula33_parte4')
from controller.pessoa_controller import PessoaController

pc = PessoaController()

for p in pc.listar_todos():
    print(p)