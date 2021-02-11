from flask_restful import  Resource

class BaseController(Resource):
    def __init__(self, dao):
        self.dao = dao

    def get(self, id= None):
        if id:
            return self.dao.buscar_por_id(id)
        return self.dao.listar_todos()

    def post(self, model):
        return self.dao.inserir(model)

    def put(self,model):
        self.carrega_parametros()
        return self.dao.inserir(model)

    def delete(self, id):
        return self.dao.deletar