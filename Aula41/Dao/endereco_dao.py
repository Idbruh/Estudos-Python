import sys
sys.path.append('/Users/900133/Documents/GitHub/TrabalhosPyhton/Aula41')
import MySQLdb

from Model.endereco_model import EnderecoModel

class EnderecoDao:
    def __init__(self):
    self.connection = MySQLdb.connect(host= "127.0.0.1", database='squad', user='root', passwd= '')
    self.cursor = self.connection.cursor()

    