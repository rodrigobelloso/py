while True:
    b = int(input("Introduzca la base (1 < b <= 10): "))
    if 1 < b <= 10:
        break
    else:
        print("Error: La base debe estar en el rango (1 < b <= 10)")

while True:
    N = int(input("Introduzca el número de dígitos (1 <= N <= 10): "))
    if 1 <= N <= 10:
        break
    else:
        print("Error: El número de dígitos debe estar en el rango (1 <= N <= 10)")

acumulador = 0

for i in range(N):
    while True:
        cifra = int(input(f"Introduzca la cifra {N - i}: "))
        if 0 <= cifra < b:
            break
        else:
            print(f"Error: La cifra debe estar en el rango [0, {b-1}]")

    acumulador += cifra * (b ** i)

print(f"El equivalente decimal es: {acumulador}")
