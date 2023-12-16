# -*- coding: utf-8 -*-
"""
Función que filtra una lista obteniendo los valores estrictamente inferiores a otro valor dado.

Para ello, se pide:

Escribir una función lista_inferiores() que
    * Recibe:
        1. una lista de valores, [x_0, x_1, x_2, ..., x_n]. (x_i int o float indistintamente)
        2. un valor límite, lim, (int o float indistintamente)
    * Devuelve:
        Una lista con los elementos que son inferiores estrictamente a lim, x_i < lim


Escribir una función solicita_lista_enteros() que:
    * Recibe:
        El número de elementos de la lista
    * Solicita al usuario los elementos de la lista
    * Devuelve:
        La lista introducida por el usuario

Escribir una función main() que:
    * Recibe:
        El número de elementos de la lista, tam
    * Solicita una lista con tam enteros
    * Solicita un valor limite
    * Obtiene la lista filtrada formada por los elementos de lista estrictamente inferiores a limite
    * Muestra por pantalla el resultado siguiendo ¡¡OBLIGATORIAMENTE!! el formato mostrado en los ejemplos

Ejemplo de ejecución para una llamada main(0):

    El número de elementos de la lista debe ser positivo.

Ejemplo de ejecución para una llamada main(5):

    Introduce los 5 elementos de la lista:
       lista[0] = 1
       lista[1] = 3
       lista[2] = 5
       lista[3] = 7
       lista[4] = 2

    Introduce el límite para filtrar: 4

    La lista [1, 3, 5, 7, 2] filtrada por el límite 4 es [1, 3, 2]
"""

# Debes completar el código de las funciones sustituyendo pass, añadiendo en su caso,
# los parámetros que sean necesarios


def lista_inferiores(listaAFiltrar, valorLim):  # 4 Pto
    listaFiltrada = []
    
    for i in range(len(listaAFiltrar)):
        if listaAFiltrar[i] < valorLim:
            listaFiltrada.append(listaAFiltrar[i])
        else:
            pass

    return listaFiltrada

def solicita_lista_enteros(tam):  # 3 Pto
    
    listaEnt = []
    
    for i in range(tam):
        valor = float(input(f"Introduce el elemento {i + 1} de {tam} de la lista: "))
        listaEnt.append(valor)
    return listaEnt 

def main(tam):  # 3 Pto
    listaAFiltrar = solicita_lista_enteros(tam)
    valorLim = int(input("Introduce el límite para filtrar: "))
    filtro = lista_inferiores(listaAFiltrar, valorLim)
    print(f"La lista {listaAFiltrar} filtrada por el límite {valorLim} es {filtro}")
    

if __name__ == '__main__':
    tam = 5
    main(tam)