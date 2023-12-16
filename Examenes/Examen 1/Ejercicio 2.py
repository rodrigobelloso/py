# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 12:50:43 2022

@author: APELLIDOS, NOMBRE (DNI)

Tipo de problema: Función que crea una lista elemento a elemento

Escribe una función crea_lista(n) que devuelve una lista con todos los
múltiplos de 3, 5 o 7 que hay en el intervalo cerrado [1, n]

"""

'''
Puntuación del ejercicio: 3 sobre 100
'''


def crea_lista(n):
    lista = []
    
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            lista.append(i)
        else:
            pass
        
    return lista


# No modificar el código a partir de aquí
if __name__ == '__main__':
    lista = crea_lista(20)
    print(lista)
    if lista == [3, 5, 6, 7, 9, 10, 12, 14, 15, 18, 20]:
        print("-------------> Correcto")
    else:
        print("Incorrecto")
    lista = crea_lista(2)
    print(lista)
    if lista == []:
        print("-------------> Correcto")
    else:
        print("Incorrecto")