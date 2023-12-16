import cmath

a = float(input("Introduce A: "))
b = float(input("Introduce B: "))
c = float(input("Introduce C: "))

if a == 0:
    if b == 0:
        print("\nLos coeficientes son absurdos.")
    else: 
        print("\nLa ecuación es de primer grado.")
        operacion = -c/b
        print(operacion)
else:
    print("\nLa ecuación es de segundo grado.")
    discriminante = b * b -4 * a * c
    if discriminante == 0:
        print("\nLas dos raíces son iguales.")
        operacion = -b / (2 * a)
        print(operacion)

    else:
        if discriminante > 0:
            print("\nLas dos raíces son reales.")
        else:
            print("\nLas dos raíces son complejas conjugadas.")
        raizDiscriminante = cmath.sqrt(discriminante)
        x1 = (-b+raizDiscriminante) / (2*a)
        x2 = (-b-raizDiscriminante) / (2*a)

        print("\nx1 = {}\nx2 = {}".format(x1, x2))  