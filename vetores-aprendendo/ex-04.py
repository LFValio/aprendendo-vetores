# Prática 4: ordenar o vetor em ordem crescente

num = []
aux = 0

# lendo os números para o vetor num
for x in range(1, 5):
    num.append(int(input(f"Número {x}: ")))

print(f"{num} # números bagunçados")

for x in range(1, 4):           # o programa precisa comparar a 1ª, 2ª e 3ª posição apenas, por isso ele repete apenas 3 vezes
    for y in range(0, 3):       # é necessário mais um for para que a posição do vetor possa ser comparada com uma acima
        if num[y] > num[x]:     # se o valor da primeira posição do vetor for maior que o próximo, eles se substituirão
            aux = num[y]        # a variável aux recebe o valor da posição 0
            num[y] = num[x]     # a posição 0 passa para a posição 1
            num[x] = aux        # a posição 1 passa para a variável auxiliar, repetindo o laço e verificando o if até que todos os números estejam em ordem

print(f"{num} # números em ordem crescente")

# no final, pode-se concluir que quando se altera as posições dos objetos da lista em repetições, ela também é alterada dentro do próprio vetor
