'''
Realice una función dibuja_curva(lista_parametros, intervalo, num_puntos)
que describe la trayectoria seguida por un móvil en el plano X-Y a lo largo del
tiempo t.

Dicha trayectoria viene dada por las siguientes ecuaciones paramétricas:

    x = cos(at) - cos(bt)^j
    y = sen(ct) - sen(dt)^k

lista_parametros:  valores de a,b,c,d,j,k almacenados por ese orden en una lista
intervalo:         lista con los valores inicial y final del tiempo t en el que
                   se debe dibujar la trayectoria del móvil
num_puntos:        número de puntos a utilizar para dibujar la gráfica


El resultado debe ser similar al contenido en el fichero 'ej1_figura.png'

Puntuación del ejercicio: 10 sobre 100
'''

import matplotlib.pyplot as plt
import numpy as np


def dibuja_curva(lista_parametros, intervalo, num_puntos):
    pass  # Sustituir pass por su solución


# No modificar a partir de esta línea
if __name__ == '__main__':
    dibuja_curva([2, 3, 2, 3, 1, 3], [0, 10], 10000)
