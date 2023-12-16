def menu():
    fo = False
    while not fo:
        print("0) Salir")
        print("1) Nuevo polinomio")
        opcion = int(input("\nOpción: "))
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
        b = int(input("Escribe b: "))
        c = int(input("Escribe c: "))
        d = int(input("Escribe d: "))
        x = int(input("Escribe x: "))

        r = poli(a, b, c, d, x)
        
        print(f"El polinomio de {a}, {b}, {c}, {d} elevado a {x} es: {r}")
