import math

def menu():
    fo = False
    while not fo:
        print("0) Salir")
        print("1) Cálculo de propiedades geométricas y repetir")
        opcion = int(input("\nOpción: "))
        if opcion < 0 or opcion > 1:
            print("Opcion inválida, repetir")
        else:
            fo = True
    return opcion

def pide_parametros():
    l_inf = float(input("Escribe el valor del lado inferior (l_inf): "))
    l_sup = float(input("Escribe el valor del lado superior (l_sup): "))
    h = float(input("Escribe el valor de la altura (h): "))
    return l_inf, l_sup, h

def calcula_area_perimetro(l_inf, l_sup, h):
    area = (l_inf + l_sup) * h / 2
    perimetro = l_inf + l_sup + (2 * math.sqrt((l_sup - l_inf)**2 + h**2))
    return area, perimetro


ff = False
while not ff:
    op = menu()
    if op == 0:
        ff = True
    elif op == 1:
        l_inf, l_sup, h = pide_parametros()
        area, perimetro = calcula_area_perimetro(l_inf, l_sup, h)
        print(f"Área del trapecio rectángulo: {area}")
        print(f"Perímetro del trapecio rectángulo: {perimetro}")