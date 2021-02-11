#  ORM
# SqlAlchemy
# --- pip3 install sqlalchemy

# Conector do Mysql
# Instalaao do conector do Mysql
# --- pip3 install mysql-connector-python

virtualenv --pytho"caminho do where python" ENV
aula53\ENV\Scripts\activate


import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
BaseModel = declarative_base()

class ProdutoModel(BaseModel):
    __tablename__ = 'Produto'
    id = id.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))
    nome = db.Column(db.String(length=200))

    def __str__(self):
        return "{},{},{}".format(self.id,self.nome,self.descricao)
    

###--- database + conector: //user:passwd@url:porta/database

conexao = db.create_engine("mysql+mysqlconnector://topskills01:ts2019@mysql.topskills.dev:3306/topskills")
criador_sessao = db.orm.session_maker()
criador_sessao.configure(bind=conexao)
sessao = criador_sessao()

#--- SELECT * agora vai retornar lista de objetos ao invés de uma tupla
sessao.query(ProdutoModel).all()

for p in produtos
    print(p.nome)  #ou print(p.__dict__)













