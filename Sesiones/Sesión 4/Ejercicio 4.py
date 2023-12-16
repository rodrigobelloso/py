while True:
    valorV = int(input("Numero de valores para el vector V: "))
    valorW = int(input("Numero de valores para el vector W: "))

    vectorV = []
    vectorW = []

    if valorV >= 0:
        for i in range (valorV):
            vectorV.append(int(input("Vector V[{}]: ".format(i))))
    else:
        print("\nEl valor introducido para el vector V no está admitido.")

    if valorW >= 0:
        for i in range (valorW):
            vectorW.append(int(input("Vector W[{}]: ".format(i))))
    else:
        print("\nEl valor introducido para el vector W no está admitido.")
        
    print("\nEl vector V completo es: {}".format(vectorV))
    print("El vector W completo es: {}\n".format(vectorW))

    productoEscalar = sum(vectorV[i] * vectorW[i] for i in range(len(vectorV)))

    print("\nEl producto escalar de los vecotres es:", productoEscalar)

    otro_calculo = input(int("¿Deseas realizar otro producto escalar? (1/0): "))
    if otro_calculo != '1':
        break