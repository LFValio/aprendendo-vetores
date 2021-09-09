# Desafio 1: criar uma tabela de partidas de futebol

times = []
aux = 0

print("----------Tabela de Partidas----------")

# vetor times recebendo strings
for x in range(1, 4):
    times.append(str(input(f"Time {x}: ")))

print("--------------Resultados--------------")

# abaixo, diferente do exercício anterior, não é necessário comparar duas posições diferentes
# basta comparar as posições iguais do mesmo vetor para criar este programa

for x in range(0, 3):       # variável x
    for y in range(0, 3):   # variável y
        if x != y:          # mostrará apenas as posições diferentes
            print(f"{times[x].ljust(10)} [ ] x [ ] {times[y]}")     # ljust utilizado apenas para a saída sair organizada

# a criação de duas variáveis (x e y) nos laços for tem apenas o objetivo de comparar os objetos do mesmo vetor
