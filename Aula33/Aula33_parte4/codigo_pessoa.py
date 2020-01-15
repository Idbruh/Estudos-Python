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




















# p1 = Pessoa()
# p1.id = 10






###-- Muda independente do valor pré-definido.
#   Orientação a objeto == estancia de classe
# p1 = Pessoa()
# p1.id = 10
# p1.nome = 'Teste'
# print(p1.id)
# print(p1.nome)
# p2 = Pessoa()
# p2.id = 11
# p2.nome = 'CAQUINHA'
# print(p2.id)
# print(p2.nome)