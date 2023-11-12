# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 17:52:49 2022

@author: jesus
"""

"""
Tipo de problema:  Sacar mensajes por pantalla

Escribe una función mensaje() que recibe como argumentos una cadena
de caracteres c y un número entero n, y muestre la cadena de caracteres
tantas veces como indique el número n, separándolas mediante guiones. Si
n es 0 o negativo, no mostrará nada por pantalla.

Ejemplo:
    Para c = 'Hola' y n = 3, mostrará: Hola - Hola - Hola
    Para c = 'Informática' y n = 1, mostrará: Informática
    Para c = 'Examen' y n = 0, no mostrará nada

"""


def mensaje(c, n):
    pass   # Sustituya pass por su solución


# No modificar el código a partir de aquí
if __name__ == '__main__':
    # Mostrar Hola - Hola - Hola
    mensaje('Hola', 3)
    # Mostrar Informática
    mensaje('Informática', 1)
    # No muestra nada si n<=0
    mensaje('Examen', 0)
