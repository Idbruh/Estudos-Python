from dao.base_dao import BaseDao
from model.cliente import Cliente

class ClienteDao(BaseDao):
    def __init__(self):
        super().__init__(Cliente)