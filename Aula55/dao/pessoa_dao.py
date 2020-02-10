from dao.base_dao import BaseDao
from model.pessoa import Pessoa

class PessoaDao(BaseDao):
    def __init___(self):
        super().__init__(Pessoa)