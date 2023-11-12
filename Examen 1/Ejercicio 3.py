# -*- coding: utf-8 -*-
"""

@autor: APELLIDOS, NOMBRE (DNI)

El valor del número e se puede calcular según la siguiente expresión:

         1      1      1     1            1
    e = ---  + ---  + --- + --- + ... +  ---
         0!     1!     2!    3!           n!

Es decir, el sumatorio de 1 / (i!), desde i=0 hasta un n concreto.

Escriba una función numero_e(n) que permita calcular el anterior sumatorio.
Utiliza la función factorial() para obtener el factorial.
"""

'''
Puntuación del ejercicio: 3 sobre 100
'''


def factorial(n):  # Función para calcular el factorial (no modificar)

    return producto


def numero_e(n):

    return r


# No modificar el código a partir de aquí
if __name__ == '__main__':
    from math import e

    print(f'El número e de la biblioteca math tiene valor {e}')

    e_5 = numero_e(5)
    print(f'El número e calculado para n=5 es {e_5}')

    if (abs(e - e_5) < 0.0017):
        print('Función aparentemente correcta para n=5.')
    else:
        print('Hay algún error en la función.')

    e_10 = numero_e(10)
    print(f'El número e calculado para n=10 es {e_10}')
    if (abs(e - numero_e(10)) < 2.74e-08):
        print('Función aparentemente correcta para n=10.')
    else:
        print('Hay algún error en la función.')