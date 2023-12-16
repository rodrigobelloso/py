print("Cálculo del perímetro. Elija una opción:\n")
print("1) Circunferencia\n2) Cuadrado\n3) Rectángulo\nOpción:")

opcion = int(input())
if opcion == 1:
    radio = float(input("Radio: "))
    perimetro = 2 * 3.14 * radio

    print("El perimetro es: ", perimetro)
    
elif opcion == 2:
    lado = float(input("Lado: "))
    perimetro = 4 * lado

    print("El perimetro es: ", perimetro)
    
elif opcion == 3:
    lado1 = float(input("Lado 1: "))
    lado2 = float(input("Lado 2: "))
    perimetro = 2 * lado1 + 2* lado2

    print("El perimetro es: ", perimetro)
else:
    print("La opcion no es correcta.")