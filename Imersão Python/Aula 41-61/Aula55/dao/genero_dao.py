from dao.base_dao import BaseDao
from model.genero import Genero

class GeneroDao(BaseDao):
    def __init__(self):
        super().__init__(Genero)
