from dao.base_dao import BaseDao
from model.autor import Autor

class AutorDao(BaseDao):
    def __init__(self):
        super().__init__(Autor)