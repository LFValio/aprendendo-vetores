# Exercício 1: Ler 7 Valores e mostrar quantos são pares e mostrar a posição dos valores.

num = []
cP = 0      # contador par
cI = 0      # contador ímpar
posP = []   # posição par
posI = []   # posição ímpar

# armazenas os valores no vetor num e os converte para inteiro
for x in range(1, 6):
    num.append(int(input(f"Valor {x}: ")))

# verificando se um número é par/ímpar, os contando e colocando-os nos vetores posP/posI.
for x in num:
    if x % 2 == 0:
        cP += 1
        posP.append(num.index(x) + 1)       # somando +1 para que comece a contar a partir da posição nº 1
    else:
        cI += 1
        posI.append(num.index(x) + 1)       # somando +1 para que comece a contar a partir da posição nº 1


# mostrando o resultado na tela
print("--------------------------Resultado:--------------------------")
print(num)
print("-------------------------Quantidades:-------------------------")
print(f"Existem {cP} pares nos valores {posP}!")
print(f"Existem {cI} ímpares nos valores {posI}!")

