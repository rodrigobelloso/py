import math

fis = False

while not fis:
    inf = float(input("Inf: "))
    sup = float(input("Sup: "))

    if inf >= sup or inf < 0:
        print("Valores no válidos")
    else:
        fis = True

listaPrimos = []
listaNoPrimos = []

for numero in range(inf, sup+1):
    esPrimo = True
    for divisor in range (2, round(math.sqrt(numero))):
        if numero % divisor == 0:
            esPrimo = False
            listaNoPrimos.append(numero)
            break
    if esPrimo:
        listaPrimos.append(numero)

print(f"En el rango dado hay {len(listaPrimos)}, que son : {listaPrimos}")
print(f"En el rango dado hay {len(listaNoPrimos)}, que son : {listaNoPrimos}")