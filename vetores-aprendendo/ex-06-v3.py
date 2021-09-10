gab = []            # vetor gabarito
nome = []           # vetor nome
res = []            # vetor resposta 1
n = []              # vetor nota
media = 0           # media da sala
c = 0

alu = int(input("Quantidade de alunos: "))          # pede a quantidade de alunos

print("----------GABARITO----------")
for x in range(1, 6):
    gab.append(str(input(f"Questão {x}: ")))             # recebe o gabarito da prova em letras

for x in range(1, alu+1):                                # fará a prova dos alunos
    print(f"----------ALUNO {x}----------")
    nome.append(str(input("Nome: ")))                    # recebe o nome do aluno
    for y in range(0, 5):
        res.append(str(input(f"Resposta {y + 1}: ")))    # recebe a resposta do aluno e guarda no vetor res
        if res[y] == gab[y]:                             # se a resposta for igual a resposta do gabarito, recebe 2 pontos
            c += 2
    n.append(c)         # o vetor n recebe as notas dos alunos
    c = 0               # o valor das notas são redefinidos
    res = []            # o vetor res é redefinido

media = (n[0] + n[1] + n[2]) / 3        # todas as notas se juntaram no vetor n, assim, utilizo os índices do
                                        # mesmo para o cálculo da média da sala

print("----------NOTAS FINAIS----------")
for x in range(0, alu+1):
    print(f"{nome[x].ljust(10)} Nota: {n[x]}")      # uso o laço for para printar o nome e a nota do aluno utilizando os vetores
print("----------MEDIA DA SALA----------")
print(f"{media:.2f}")                               # printa a média da sala
