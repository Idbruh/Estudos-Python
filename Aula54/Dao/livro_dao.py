class LivroDao(BaseDao):
    def __init__(self):
        super().__init__("Livro")

    def listar_todos(self):
        tuplas = super().listar_todos()
        lista = []
        for l in tuplas:
            model = LivroDao(l[1], l[2],l[0])
            lista.append(model.__dict__)