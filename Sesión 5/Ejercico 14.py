TAM_MAX = 20

fll = False

while not fll:
    lado1 = int(input("Escribe el lado 1: "))
    lado2 = int(input("Escribe el lado 2: "))

    if lado1 < 1 and lado1 > TAM_MAX or lado2 < 1 or lado2 > TAM_MAX:
        print("Los lados no son correctos.")
    else:
        fll = True

for i in range(0, lado1):
    for j in range(0, lado2):
        if i == 0 or i == lado1-1 or j == 0 or j == lado2-1 or i==j or i== lado2-1-j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()