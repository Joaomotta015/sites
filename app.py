from aluno import Aluno
from jurado import Jurado
 
class ConcursoQuadrilha:
    def __init__(self):
        self.alunos = {}
        self.jurados = []
        self.resultados = {}
 
    def cadastrar_aluno(self, nome, categoria):
        self.alunos[nome] = Aluno(nome, categoria)
 
    def adicionar_jurado(self, nome_jurado):
        self.jurados.append(Jurado(nome_jurado))
 
    def votar(self, nome_aluno, nome_jurado, elegancia, desenvoltura, simpatia, reciclavel):
        aluno = self.alunos.get(nome_aluno)
        if not aluno:
            print(f'{nome_aluno} não está cadastrado.')
            return
        jurado = next((j for j in self.jurados if j.nome == nome_jurado), None)
        if not jurado:
            print(f'{nome_jurado} não está autorizado a votar.')
            return
        jurado.votar(aluno, elegancia, desenvoltura, simpatia, reciclavel)
 
    def calcular_resultados(self):
        for aluno in self.alunos.values():
            media = aluno.calcular_media()
            if media:
                self.resultados[aluno.nome] = {
                    'media_elegancia': media['media_elegancia'],
                    'media_desenvoltura': media['media_desenvoltura'],
                    'media_simpatia': media['media_simpatia'],
                    'media_reciclavel': media['media_reciclavel'],
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
 
    def mostrar_jurados(self):
        print("\nJurados do Concurso:\n")
        for jurado in self.jurados:
            print(jurado.mostrar_info())
 
# Exemplo de uso:
if __name__ == "__main__":
    concurso = ConcursoQuadrilha()
 
    # Cadastro de alunos
    concurso.cadastrar_aluno('Beatriz', 'Miss')
    concurso.cadastrar_aluno('Mateus', 'Mister')
    concurso.cadastrar_aluno('Bruno Arantes', 'Mister')
    concurso.cadastrar_aluno('Bruno Oliveira', 'Mister')
    concurso.cadastrar_aluno('Daniela', 'Miss')
    concurso.cadastrar_aluno('Stefany', 'Miss')
 
    # Adição de jurados
    concurso.adicionar_jurado('Jurado 1')
    concurso.adicionar_jurado('Jurado 2')
 
    # Simulação de votação
    concurso.votar('Beatriz', 'Jurado 1', 9.5, 8.0, 7.5, 6.5)
    concurso.votar('Beatriz', 'Jurado 2', 8.5, 7.0, 8.0, 6.0)
    concurso.votar('Mateus', 'Jurado 1', 8.0, 9.0, 7.0, 8.0)
    concurso.votar('Mateus', 'Jurado 2', 7.5, 8.5, 7.5, 7.5)
    concurso.votar('Bruno Arantes', 'Jurado 1', 7.0, 8.5, 8.5, 7.0)
    concurso.votar('Bruno Arantes', 'Jurado 2', 7.5, 8.0, 8.0, 6.5)
    concurso.votar('Bruno Oliveira', 'Jurado 1', 8.0, 7.5, 8.0, 7.5)
    concurso.votar('Bruno Oliveira', 'Jurado 2', 7.0, 8.0, 7.5, 7.0)
    concurso.votar('Daniela', 'Jurado 1', 8.5, 9.0, 7.5, 8.5)
    concurso.votar('Daniela', 'Jurado 2', 7.5, 8.0, 8.0, 7.0)
    concurso.votar('Stefany', 'Jurado 1', 8.0, 8.5, 8.0, 7.5)
    concurso.votar('Stefany', 'Jurado 2', 7.0, 8.0, 7.5, 6.5)
 
    # Calcular e mostrar resultados
    concurso.calcular_resultados()
    concurso.mostrar_resultados()