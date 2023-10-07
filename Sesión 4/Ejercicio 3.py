base = 0
basemin = 2
basemax = 10

while base > basemax or base < basemin:
    mes = int(input("Introduce una base ({}-{}): ".format(basemin, basemax)))
    if base > 10 or base < 2:
        print("La base introducida es incorrecta. Escribe una base comprendida entre {} y {}.\n".format(basemin, basemax))
        break

print("La base {} es válida.".format(base))


