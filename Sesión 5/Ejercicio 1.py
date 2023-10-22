n = int(input("Escribe un número máximo de valores: "))

lista = []

for i in range(n):
    valor = int(input(f"Valor[{i+1}]= "))
    lista.append(valor)

sumaPositivos = 0
contadorPositivos = 0

for valor in lista:
    if valor > 0:
        sumaPositivos += valor
        contadorPositivos += 1

print(f"La lista de valores es: {lista}.")

print(f"Se escribieron {contadorPositivos} valores positivos.")
print(f"La suma es {sumaPositivos}.")