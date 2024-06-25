class Aluno:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.notas = {}

    def adicionar_nota(self, nome_jurado, elegancia, desenvoltura, simpatia, reciclavel):
        self.notas[nome_jurado] = {
            'elegancia': elegancia,
            'desenvoltura': desenvoltura,
            'simpatia': simpatia,
            'reciclavel': reciclavel
        }

    def calcular_media(self):
        if not self.notas:
            return None
        num_jurados = len(self.notas)
        media_elegancia = sum(self.notas[jurado]['elegancia'] for jurado in self.notas) / num_jurados
        media_desenvoltura = sum(self.notas[jurado]['desenvoltura'] for jurado in self.notas) / num_jurados
        media_simpatia = sum(self.notas[jurado]['simpatia'] for jurado in self.notas) / num_jurados
        media_reciclavel = sum(self.notas[jurado]['reciclavel'] for jurado in self.notas) / num_jurados
        return {
            'media_elegancia': media_elegancia,
            'media_desenvoltura': media_desenvoltura,
            'media_simpatia': media_simpatia,
            'media_reciclavel': media_reciclavel
        }
