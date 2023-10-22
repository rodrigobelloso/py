minimo = float('inf')
maximo = float('-inf')

while True:
    
    numero = float(input("Escribe un número positivo (o uno negativo para salir): "))
    if numero < 0:
        break
    else:
        minimo = min(minimo, numero)
        maximo = max(maximo, numero)
        print(f"Valor mínimo: {minimo}, Valor máximo: {maximo}")

print("Se ha detenido el programa porque se ha introducido un numero negativo.")
