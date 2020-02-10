from Model.pessoa_model import Pessoa
from Dao.base_dao import BaseDao



class PessoaDao:
    def list_all(self):
        return self.sessao.query(Pessoa).all()

    def buscar_por_id(self, id):
        return self.sessao.query(Pessoa).filter_by(id=id)

    def deletar(self,id):
        model = self.sessao.query(Pessoa).filter_by(id=id)
        self.sessao.delete(model)
        self.sessao.commit()
        return f"Deletando o obj de ID {}"