n = int(input("Escribe un número máximo de valores: "))

sumaPositivos = 0
contadorPositivos = 0

for i in range(n):
    valor = int(input(f"Ingrese el valor {i + 1}: "))
    if valor > 0:
        sumaPositivos += valor
        contadorPositivos += 1

print(f"Se escribieron {contadorPositivos} valores positivos.")
print(f"La suma es {sumaPositivos}.")