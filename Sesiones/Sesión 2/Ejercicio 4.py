num = int(input("Introduce un numero: "))

if 100 <= num <= 999:
    c = num // 100
    u = num % 10
    
    if c == u:
        print("El numero {} es capicua.".format(num))
    else:
        print("El numero {} no es capicua.".format(num))
else:
    print("El numero no se encuentra en el rango.")