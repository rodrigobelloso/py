def menu():
    fo = False
    while not fo:
        print("0) Salir")
        print("1) Nuevo polinomio")
        opcion = int(input("Opción: "))
        if opcion < 0 or opcion > 1:
            print("Opcion inválida, repetir")
        
        else:
            fo = True
            
    return opcion

def poli(a, b , c, d, x):
    res = a * x**3 + b * x**2 + c * x + d 
    return res

ff = False
while not ff:
    op = menu()
    if op == 0:
        ff = True
    elif op == 1:
        a = int(input("Escribe a: "))
        b = int(input("Escribe a: "))
        c = int(input("Escribe a: "))
        d = int(input("Escribe a: "))
        x = int(input("Escribe a: "))
        r = poli(a, b, c, d, x)
        
        print(r)
