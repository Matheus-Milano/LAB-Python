"""Nathan Mazzaro Pereira"""
class Aluno:
    """Criar objetos"""
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __repr__(self):
        return f"\nNome: {self.nome}\nMatrícula: {self.matricula}"
    
class Turma:
    """Criar objetos"""
    def __init__(self, nome_turma, capacidade_max):
        self.nome_turma = nome_turma
        self.capacidade_max = capacidade_max
        self.alunos = []
    """Matricular alunos na turma"""
    def matricular_aluno(self, aluno):
        if len(self.alunos) >= self.capacidade_max:
            print("A sala está cheia!")
        else:
            self.alunos.append(aluno)
            print(f"Aluno {aluno.nome} matriculado com sucesso!")
    """Listar os alunos da turma"""
    def listar_alunos(self):
        for aluno in self.alunos:
            print(aluno)

turma1 = Turma("A", 2)
nathan = Aluno("Nathan", "1234")
bulacha = Aluno("Bulacha", "1243")
leon = Aluno("Leon", "2134")
Turma.matricular_aluno(turma1, nathan)
Turma.matricular_aluno(turma1, bulacha)
Turma.matricular_aluno(turma1, leon)
Turma.listar_alunos(turma1)
