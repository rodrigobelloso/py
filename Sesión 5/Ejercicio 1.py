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

print(f"Se introdujo la lista de valores {lista}.")

print(f"Se introdujeron {contadorPositivos} valores positivos.")
print(f"Su suma es {sumaPositivos}.")
