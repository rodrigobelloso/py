VALOR_MINIMO = 0
VALOR_MAXIMO = 1e6
N_MAX_ITER = 20

print("Piense un numero entre 0 y 1.000.000")
print("Lo adivinaré en un máximo de 20 intentos.")

inf = VALOR_MINIMO
sup = VALOR_MAXIMO
encontrado = False
contador = 0

while not encontrado and contador < N_MAX_ITER:
    num = ((inf+sup) // 2)
    print(f"Es el {num}?\n(Si es mayor pulse > \nSi es menor pulse <\nSi ha acertado pulse =)")
    respuesta = str(input())
    if respuesta == '>':
        inf = num + 1

    elif respuesta == '<':
        sup = num - 1

    elif respuesta == '=':
        encontrado = True

    contador += 1

if encontrado:
    print("Acertado el numero {} en {} intentos.".format(num, contador))
else:
    print("Alguna respuesta equivocada.")