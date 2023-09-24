# Solicitud de datos
base = int(input("Introduce la base de un numero: "))

# Comprobacón de rango de la base
if 2 <= base <= 10:
    cifra1 = int(input("\nIntroduce la primera cifra del número: "))
    cifra2 = int(input("Introduce la segunda cifra del número: "))
    cifra3 = int(input("Introduce la tercera cifra del número: "))
    cifra4 = int(input("Introduce la cuarta cifra del número: "))

    # Comprobación de rango de las cifras introducidas
    if (cifra1 >= 0 and cifra1 <= base - 1) and (cifra2 >= 0 and cifra2 <= base - 1) and (cifra3 >= 0 and cifra3 <= base - 1) and (cifra3 >= 0 and cifra3 <= base - 1):
        
        # Cálculos
        dec = cifra1 * base * 3 + cifra2 * base * 2 + cifra3 * base * 1 + cifra4 * base * 0
        print("\nLa base es:", dec, "\n")

    else:
        print("\nUna cifra no corresponde con el rango establecido (0-{}).\n".format(base - 1))

else:
    print("\nEl número {} no corresponde con el rango establecido (2-10).\n".format(base))