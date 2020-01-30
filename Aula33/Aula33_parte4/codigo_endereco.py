import sys
#importando biblioteca com interação nas pastas do sistema
sys.path.append('/Users/900133/Documents/GitHub/TrabalhosPyhton/Aula33/Aula33_parte4')
import sys
sys.path.append('/Users/900133/Documents/GitHub/TrabalhosPyhton/Aula33/Aula33_parte4')
from model.endereco import Endereco
from Dao.enderecodb import EnderecoDb

e = Endereco()
e_db = EnderecoDb()

lec = e_db.listar_todos()

#lpc = e_db.converter_tabela_dicionario_classe(lpt)
e.exportar_txt(lec)