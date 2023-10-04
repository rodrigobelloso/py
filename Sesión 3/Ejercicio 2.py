 # Listas iniciales
lista = [3, 5, 1, 7, 9, 2, 9, 6, 8]
listaAux = []

# 1) Añadir a lista_aux el último elemento de lista
listaAux.append(lista[-1])

# 2. Borrar el último elemento de lista
lista.pop()

# 3. Si lista tiene su valor máximo repetido:
maxValor = max(lista)
if lista.count(maxValor) > 1:
    lista.remove(maxValor)
    listaAux.append(maxValor)

# 4. Se elimina el mínimo de lista
minValor = min(lista)
lista.remove(minValor)
print(minValor)

# 5. Se inserta el mínimo anterior en la primera posición de lista_aux
listaAux.insert(0, minValor)

# 6. Si el último elemento de lista es mayor que el primero, se invierte el orden de lista
if lista[-1] > lista[0]:
    lista.reverse()

# 7. Se intercambia el primer elemento con el mínimo de lista.
lista[0], lista[lista.index(minValor)] = minValor, lista[0]

# 8. Si el valor 2 está en lista se borra de lista y se añade en lista_aux
if 2 in lista:
    lista.remove(2)
    listaAux.append(2)

# 9. Añadir al final de lista_aux la secuencia del 10 al 1.
listaAux.extend(range(10, 0, -1))

# 10. Devolver ambas listas.
print("Lista:", lista)
print("Lista auxiliar:", listaAux)
