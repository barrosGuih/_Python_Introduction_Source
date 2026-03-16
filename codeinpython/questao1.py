class Aluno:
    def __init__(self, nome, matricula, n1, n2, n3):
        self.nome = nome
        self.matricula = matricula
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
    
alunos = []
todasAsNotas = []

print("Informe os dados dos Alunos: ")

for i in range(3):
    nome = input("\nDigite seu nome: ")
    matricula = int(input("Digite sua matricula: "))
    n1 = float(input("Digite sua nota 1: "))
    n2 = float(input("Digite sua nota 2: "))
    n3 = float(input("Digite sua nota 3: "))
    
    aluno = Aluno(nome, matricula, n1, n2, n3)
    alunos.append(aluno)
    
    todasAsNotas.extend([n1, n2, n3])

for aluno in alunos:
    mediaArit = (aluno.n1 + aluno.n2 + aluno.n3) / 3
    mediaPond = ((aluno.n1 * 0.6) + (aluno.n2 * 0.2) + (aluno.n3 * 0.2))
    print("\n============================================")
    
    print(f"\nnome do aluno: {aluno.nome}")
    print(f"Matricula: {aluno.matricula}")
    print(f"Media aritmetica de: {mediaArit:.2f}")
    print(f"Media ponderada de: {mediaPond:.2f}")
    
maior = max(todasAsNotas)
menor = min(todasAsNotas)
media_turma = (sum(todasAsNotas)) / len(todasAsNotas)

print("\nEstatisticas da turma:\n")
print(f"A maior nota e: {maior}") 
print(f"A menor nota e: {menor}")
print(f"A media da turma e: {media_turma}")
    