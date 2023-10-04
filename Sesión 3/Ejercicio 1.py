# Lista inicial
lista = [3, 4, 5, 6]

# Solicitar un índice
indice = int(input("Introduce un índice para actualizar (0 a {}): ".format(len(lista) - 1)))

# Comprobar si el índice es válido
if -len(lista) <= indice < len(lista):
    # Solicitar el nuevo valor
    nuevoValor = int(input("\nEscribe un nuevo valor: "))
    
    # Actualizar el elemento en la lista
    lista[indice] = nuevoValor
    
    # Devolver la lista modificada
    print("\nLa nueva lista es:", lista)
else:
    print("\nEl indice se encuentra fuera de la lista.\n")
