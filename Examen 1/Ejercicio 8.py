# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 18:00:51 2022

@author: jesus
"""

"""
Tipo de problema:  Petición de datos para una lista hasta que se introduzca un 0

Escribe un script que pida datos continuamente hasta que se introduzca un 0.
Cada dato lo irá introduciendo en una lista. Al finalizar, debe indicar
cuántos datos se han introducido y la lista generada.

Ejemplo de interacción programa-usuario:
    Introduzca un dato (0 para finalizar): 5
    Introduzca un dato (0 para finalizar): 9
    Introduzca un dato (0 para finalizar): 2
    Introduzca un dato (0 para finalizar): 8
    Introduzca un dato (0 para finalizar): 0
    Finalizado. Has introducido 4 datos: [5, 9, 2, 8]


"""
num = 1
lista = []

while num != 0:
    num = int(input("Introduzca un dato (0 para finalizar): "))
    
    if num == 0:
        print(f"Finalizado. Has introducido {len(lista)} datos: {lista}")
        break
    else:
        lista.append(num)