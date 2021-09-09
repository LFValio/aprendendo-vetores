gab = []        # vetor gabarito
nome = []       # vetor nome
res1 = []       # vetor resposta 1
res2 = []       # vetor resposta 2
res3 = []       # vetor resposta 3
n1 = 0          # nota 1
n2 = 0          # nota 2
n3 = 0          # nota 3
n = []          # vetor nota
media = 0       # media da sala


def nota(a, b, c, num):                                 # criação de uma função para não ser necessário repetir o código
    print(f"----------ALUNO {num}----------")           # das provas dos alunos várias vezes
    a.append(str(input("Nome: ")))
    for r in range(0, 5):
        b.append(str(input(f"Resposta {r + 1}: ")))
        if b[r] == gab[r]:
            c += 2
    return c


print("----------GABARITO----------")
for x in range(1, 6):
    gab.append(str(input(f"Questão {x}: ")))        # recebe o gabarito da prova em letras

n.append(nota(nome, res1, n1, 1))       # aluno 1 --> recebe o nome, resposta, nota e o número do aluno

n.append(nota(nome, res2, n2, 2))       # aluno 2 --> recebe o nome, resposta, nota e o número do aluno

n.append(nota(nome, res3, n3, 3))       # aluno 3 --> recebe o nome, resposta, nota e o número do aluno.

media = (n[0] + n[1] + n[2]) / 3        # todas as notas se juntaram no vetor n, assim, utilizo os índices do mesmo para o cálculo da média da sala

print("----------NOTAS FINAIS----------")
for x in range(0, 3):
    print(f"{nome[x].ljust(10)} Nota: {n[x]}")      # uso o laço for para printar o nome e a nota do aluno utilizando os vetores
print("----------MEDIA DA SALA----------")
print(f"{media:.2f}")
