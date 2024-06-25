concurso = ConcursoQuadrilha()

concurso.cadastrar_aluno('Beatriz', 'miss')
concurso.cadastrar_aluno('Mateus', 'mister')
concurso.cadastrar_aluno('Bruno Arantes', 'mister')
concurso.cadastrar_aluno('Bruno Oliveira', 'mister')
concurso.cadastrar_aluno('Daniela', 'miss')
concurso.cadastrar_aluno('Stefany', 'miss')

concurso.adicionar_jurado('Jurado 1')
concurso.adicionar_jurado('Jurado 2')

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

concurso.calcular_resultados()
concurso.mostrar_resultados()
iolio
lll ffffff