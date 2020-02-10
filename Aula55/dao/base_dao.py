import sqlalchemy as db
from sqlalchemy.orm.session import sessionmaker


class BaseDao:
    def __init__(self, table,):
        self.table = table
        engine = create_engine("mysql+mysqlconnector://user=")
        session_mk = sessionmaker()
        session_mk.configure = sessionmaker(bind = engine)
        self.session = session_mk()


    def list_all(self):
        list = []
        list_model = self.session.query(self.table).all()
        for m in list_model:
            list_model.append(list)
        return list


    def get_by_id(self, id):
        list_model = self.session.query(self.table).filter_by(id).one()
        return f""


    def insert(self, model):


    def update(self, model):
        self.session.merge(model)
        self.session.commit()

    def delete(self, id):
        self.session.delete(self.get_by_id(id))
        self.session.commit()
        return f"objeto {id} DELETADO"

