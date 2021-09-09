# Exercício 3: ler vários nomes mas só armazenar aqueles que começam com C.

nome = []
cNome = 0       # contagem nome
sNome = []      # string nome

for x in range(1, 6):
    nome.append(str(input(f"{x}º Nome: ")))

for x in nome:                   # varrerá o vetor nome, verificando todas as palavras que contém nele
    if x[0].lower() == "c":      # x[0].lower() --> pega o primeiro caractere e o converte em minúsculo
        cNome += 1
        sNome.append(x)          # as strings que tiverem "C" ficarão armazenadas no vetor sNome

print(f"{cNome} nomes começam com C, sendo eles: {sNome}")
