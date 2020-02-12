from dao.base_dao import BaseDao
from model.livro import Livro

class LivroDao(BaseDao):
    def __init__(self):
        super().__init__(Livro)
