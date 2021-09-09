# Exercícios 2: Listagem de 4 alunos, 2 provas e média de cada um.

alu = []        # alunos
n1 = []         # nota 1
n2 = []         # nota 2
m = []          # média por aluno
aluA = 0        # aluno acima da média
mSoma = 0       # media soma (soma de todas as médias da sala)

# colocar as informações em vetores, onde o nome é convertido para string e as notas para float
for x in range(1, 5):
    alu.append(str(input(f"Aluno {x}: ")))
    n1.append(float(input(f"Nota 1: ")))
    n2.append(float(input(f"Nota 2: ")))
    print("----------------------------")

# juntar todas as médias no vetor m
for x in range(0, 4):
    m.append((n1[x] + n2[x]) / 2)

# somas todas as médias para mais tarde calcular a média da sala
for x in m:
    mSoma += x

# cálculo da média da sala
mediaSala = mSoma / len(m)

# mostrar o resultado ao usuário
for x in range(0, 4):
    print(f"O aluno {alu[x]} tirou média {m[x]}!")
    if m[x] > mediaSala:
        aluA += 1

print(f"Houve {aluA} alunos acima da média da sala ({mediaSala})")
