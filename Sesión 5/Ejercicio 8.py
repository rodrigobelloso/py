baseMin = 1
baseMax = 10

while True:
    b = int(input(f"Introduzca una base [{baseMin}-{baseMax}]: "))
    if baseMin < b <= baseMax:
        break
    else:
        print(f"Error: La base debe estar en el rango [{baseMin}-{baseMax}].")

while True:
    n = int(input(f"Introduzca el número de dígitos [{baseMin}-{baseMax}]: "))
    if baseMin <= n <= baseMax:
        break
    else:
        print(f"Error: El número de dígitos debe estar en el rango [{baseMin}-{baseMax}].")

acumulador = 0

for i in range(n):
    while True:
        cifra = int(input(f"Introduzca la cifra {n - i} [0 - {b-1}]: "))
        if 0 <= cifra < b:
            break
        else:
            print(f"Error: La cifra debe estar en el rango [0, {b-1}]")

    acumulador += cifra * (b ** i)

print(f"El equivalente decimal es: {acumulador}")