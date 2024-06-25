class Jurado:
    def __init__(self, nome):
        self.nome = nome

    def esta_autorizado(self, concurso):
        return self.nome in concurso.jurados
