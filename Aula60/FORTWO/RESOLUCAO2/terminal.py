from Aula60.ForTwo.r2.local import Local

class Terminal(Local):
    def __init__(self):
        pessoas = [
                        'piloto', 'oficial1', 'oficial2'
                        ,'chefe de serviço', 'comissário1', 'comissário2'
                        ,'policial', 'presidiario'
                    ]

        super().__init__(pessoas)