def menu():
    fo = False
    while not fo:
        print("0) Salir")
        print("1) 10 impares y salir")
        print("2) Impares divisibles entre 3 o entre 7 y repetir")
        opcion = int(input("Opción: "))
        if opcion < 0 or opcion > 2:
            print("Opcion inválida, repetir")
        
        else:
            fo = True
            
    return opcion

ff = False
while not ff:
    op = menu()
    if op == 0:
        ff = True
    elif op == 1:
        for i in range(10):
            print(2*i + 1, end=' ')
        ff = True
    elif op == 2:
        for i in range(1, 300):
            if i%3 == 0 or i%7:
                print(i, end=' ')