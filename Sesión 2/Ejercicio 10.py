# Solicitud de datos de la primera fracción
num1 = float(input("Introduce el primer numerador: "))
den1 = float(input("Introduce el primer denominador: "))

# Solicitud de datos de la segunda fracción
num2 = float(input("Introduce el segundo numerador: "))
den2 = float(input("Introduce el segundo denominador: "))

# Condición de denominador equivalente a 0
if den1 != 0 and den2 != 0:

    # Menú para elegir la operacón
    print("\nOperaciones con fracciones. Elija una opción:\n")
    print("1) Suma\n2) Resta\n3) Multiplicación\n4) División\n")
    opcion = int(input("Opción: "))

    # Cálculo suma
    if opcion == 1:
        sumaNumerador = num1 * den2 + num2 * den2
        sumaDenominador = den1 * den2
        print("\nEl resultado de la suma es: {}/{}\n".format(sumaNumerador, sumaDenominador))
    
    # Cálculo resta
    elif opcion == 2:
        restaNumerador = num1 * den2 - num2 * den2
        restaDenominador = den1 * den2
        print("\nEl resultado de la resta es: {}/{}\n".format(restaNumerador, restaDenominador))
        
    # Cálculo multiplicación
    elif opcion == 3:
        multiplicacionNumerador = num1 * num2
        multiplicacionDenominador = den1 * den2
        print("\nEl resultado de la multiplicación es: {}/{}\n".format(multiplicacionNumerador, multiplicacionDenominador))

    # Cálculo división
    elif opcion == 4:
        divisionNumerador = num1 * den2
        divisionDenominador = num2 * den1
        print("\nEl resultado de la división es: {}/{}\n".format(divisionNumerador, divisionDenominador))

    # Condición de opción inexistente
    else:
        print("\nSe ha escogido una opción inválida. El programa se ha detenido.")

else:
    print("\nSe ha introducido un denominador con valor 0. El programa se ha detenido.")