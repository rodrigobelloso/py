lista = [3, 4, 5, 6]

indice = int(input("Introduce un índice para actualizar (0 a {}): ".format(len(lista) - 1)))

if -len(lista) <= indice < len(lista):

    nuevoValor = int(input("\nEscribe un nuevo valor: "))

    lista[indice] = nuevoValor

    print("\nLa nueva lista es:", lista)
else:
    print("\nEl indice se encuentra fuera de la lista.\n")