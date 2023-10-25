import math

num = int(input("Escribe un numero: "))

maxTol = 0.001
minTol = 0
cont = 0

while True:
    tol = float(input(f"Introduzca una tolerancia [{minTol}-{maxTol}]: "))

    if tol > maxTol:
        tol = maxTol

    elif tol <= minTol:
        print(f"Error: La tolerancia debe estar entre el rango [{minTol}-{maxTol}].")

    else:
        break

while ops < tol:
    cont += 1
    numTol = int(input("Escriba un número para hallar su tolerancia: "))

    ops = abs((num-numTol)/num)

    if numTol < 0:
        menor = abs(math.sqrt(numTol))
        print(f"{menor}i")
    
    else:
        print (ops)