class ConcursoQuadrilha:
    def __init__(self):
        self.alunos = []
        self.jurados = []
        self.resultados = {}

    def cadastrar_aluno(self, nome, categoria):
        aluno = Aluno(nome, categoria)
        self.alunos.append(aluno)

    def adicionar_jurado(self, nome_jurado):
        jurado = Jurado(nome_jurado)
        self.jurados.append(jurado.nome)

    def votar(self, nome_aluno, nome_jurado, elegancia, desenvoltura, simpatia, reciclavel):
        aluno = next((a for a in self.alunos if a.nome == nome_aluno), None)
        if not aluno:
            print(f'{nome_aluno} não está cadastrado.')
            return
        
        jurado = Jurado(nome_jurado)
        if not jurado.esta_autorizado(self):
            print(f'{nome_jurado} não está autorizado a votar.')
            return
        
        aluno.adicionar_nota(nome_jurado, elegancia, desenvoltura, simpatia, reciclavel)

    def calcular_resultados(self):
        for aluno in self.alunos:
            media_notas = aluno.calcular_media()
            if media_notas:
                self.resultados[aluno.nome] = {
                    'media_elegancia': media_notas['media_elegancia'],
                    'media_desenvoltura': media_notas['media_desenvoltura'],
                    'media_simpatia': media_notas['media_simpatia'],
                    'media_reciclavel': media_notas['media_reciclavel'],
                    'jurados': list(aluno.notas.keys())
                }

    def mostrar_resultados(self):
        print("\nResultados do Concurso de Quadrilha:\n")
        for aluno, info in self.resultados.items():
            print(f"Aluno: {aluno}")
            print(f"  Média Elegância: {info['media_elegancia']:.1f}")
            print(f"  Média Desenvoltura: {info['media_desenvoltura']:.1f}")
            print(f"  Média Simpatia: {info['media_simpatia']:.1f}")
            print(f"  Média Reciclável: {info['media_reciclavel']:.1f}")
            print(f"  Jurados que votaram: {', '.join(info['jurados'])}\n")
