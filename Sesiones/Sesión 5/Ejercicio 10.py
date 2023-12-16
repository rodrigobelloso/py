numero = int(input("Número a comprobar si es primo: "))

esPrimo = True

if numero >= 1:
    for i in range(2, numero):
        if numero % i == 0:
            esPrimo = False
            divisor = i
            break

    if esPrimo:
        print(f"El número {numero} es primo.")

    else:
        print(f"El número {numero} no es primo, ya que es divisible entre {divisor}")

else:
    print("El número introducido no corresponde con el rango deseado.")