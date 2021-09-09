gab = []
nome = []
res1 = []
res2 = []
res3 = []
n1 = 0
n2 = 0
n3 = 0
n = []
media = 0

print(f"----------ALUNO 1----------")
nome.append(str(input("Nome: ")))
for x in range(0, 5):
    res1.append(str(input(f"Resposta {x+1}: ")))
    if res1[x] == gab[x]:
        n1 += 2
n.append(n1)

print(f"----------ALUNO 2----------")
nome.append(str(input("Nome: ")))
for x in range(0, 5):
    res2.append(str(input(f"Resposta {x+1}: ")))
    if res2[x] == gab[x]:
        n2 += 2
n.append(n2)

print(f"----------ALUNO 3----------")
nome.append(str(input("Nome: ")))
for x in range(0, 5):
    res3.append(str(input(f"Resposta {x+1}: ")))
    if res3[x] == gab[x]:
        n3 += 2
n.append(n3)

media = (n1 + n2 + n3) / 3

print("----------NOTAS FINAIS----------")
for x in range(0, 3):
    print(f"{nome[x].ljust(10)} Nota: {n[x]}")
print("----------MEDIA DA SALA----------")
print(f"{media:.2f}")
