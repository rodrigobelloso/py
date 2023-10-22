n = int(input("Ingrese un número entero: "))

contador = 0

while n % 2 == 0:
    m = n // 2
    contador += 1

print(f"El número {n} es divisible entre 2 {contador} veces.")