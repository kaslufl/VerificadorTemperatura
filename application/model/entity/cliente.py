class Cliente:

    def __init__(self, nome = None):
        self._nome = nome
    
    def get_id(self):
        return self._id
    
    def get_nome(self):
        return self._nome

    def set_id(self, id):
        self._id = id
    
    def set_nome(self, nome):
        self._nome = nome