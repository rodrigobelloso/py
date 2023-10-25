lista = [3, 5, 1, 7, 9, 2, 9, 6, 8]
listaAux = []

listaAux.append(lista[-1])

lista.pop()

maxValor = max(lista)
if lista.count(maxValor) > 1:
    lista.remove(maxValor)
    listaAux.append(maxValor)

minValor = min(lista)
lista.remove(minValor)

listaAux.insert(0, minValor)

if lista[-1] > lista[0]:
    lista.reverse()

lista[0], lista[lista.index(minValor)] = minValor, lista[0]

if 2 in lista:
    lista.remove(2)
    listaAux.append(2)

listaAux.extend(range(10, 0, -1))

print("Lista:", lista)
print("Lista auxiliar:", listaAux)
