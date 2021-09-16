fil = []
num = []
peg = ["---"]

for x in range(0, 10):
    num.append(x)

for x in range(1, 11):
    fil.append(f"B{x}")

fin = False
while not fin:
    print(f"\n{fil}")
    print("-------------------------------------------------------------")

    res = int(input("Reservar a cadeira: B"))
    for x in range(0, 10):
        if res-1 == num[x]:
            fil[x] = peg[0]

    print(f"\n{fil}")

    esc = str.upper((input("Deseja reservar outra cadeira?\n\n[S]im/[N]ão\n\n")))
    if esc == "N":
        print("Até logo!")
        fin = True
