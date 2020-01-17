import sys
sys.path.append('/Users/mdgranemann/Documents/Github/AlunosPython/TrabalhosPython/36-Aula36')
from Controller.endereco_controller import EnderecoController
from Model.endereco import Endereco

end = Endereco()
end.logradouro = 'Rua dos Pombos123'
end.numero = '0'
end.complemento = 'casa muito engraçada'
end.bairro = 'sem nome'
end.cidade = 'gaspar'
end.cep = '11111-000'
end.id = 123

contr=  EnderecoController()
id_salvo = contr.salvar(end)
print(contr.buscar_por_id(id_salvo))