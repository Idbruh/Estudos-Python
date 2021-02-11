import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base


from Dao.livro_dao import LivroDao

dao = LivroDao()
livros = dao.listar_todos()
for l in livros:
    print(l)
