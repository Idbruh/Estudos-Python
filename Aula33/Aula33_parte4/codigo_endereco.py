import sys
#importando biblioteca com interação nas pastas do sistema
sys.path.append('/Users/900133/Documents/GitHub/TrabalhosPyhton/Aula33/Aula33_parte4')

from model.pessoa import Pessoa
from dao.pessoadb import PessoaDb

p = Pessoa()
p_db = PessoaDb()

lpc = p_db.listar_todos()
# lpc = p_db.converter_tabela_dicionario_classe(lpt)
p.exportar_txt(lpc)