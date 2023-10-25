base = 0
baseMin = 2
baseMax = 10

while baseMin <= base or base <= baseMax:
    base = int(input("Introduce una base ({}-{}): ".format(baseMin, baseMax)))
    if base >= baseMax or base <= baseMin:
        print("\nLa base introducida ({}) es incorrecta. Escribe una base comprendida entre {} y {}.\n".format(base, baseMin, baseMax))
    else:
        baseB = int(input("Introduce un número entero en base {} (positivo o 0): ".format(base)))
        if baseB >= 0:
            numeroAux = baseB;
            digitos = []

            while numeroAux > 0:
                digitoLista = numeroAux % 10
                if digitoLista >= base:
                    print("Error: El dígito {} no está en el rango [0, {base - 1}]" .format(digitoLista))
                digitos.insert(0, digitoLista)
                numeroAux //= 10
                break
            print(f"Dígitos en base {base}: {digitos}")
            decimal = 0
            for i in range(len(digitos)):
                decimal += digitos[i] * (base ** i)

            print(f"Equivalente en base 10: {decimal}")

        else:
            print("El número introducido 5tiene que ser superior a 0. Inténtalo de nuevo.")