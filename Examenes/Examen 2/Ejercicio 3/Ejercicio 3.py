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


El resultado debe ser similar al contenido en el fichero 'Resultado.png'

Puntuación del ejercicio: 10 sobre 100
'''

import matplotlib.pyplot as plt
import numpy as np


def dibuja_curva(lista_parametros, intervalo, num_puntos):
    a = lista_parametros[0]
    b = lista_parametros[1]
    c = lista_parametros[2]
    d = lista_parametros[3]
    j = lista_parametros[4]
    k = lista_parametros[5]

    t_min, t_max = intervalo
    t = np.linspace(t_min, t_max, num_puntos)

    x = np.cos(a * t) - np.cos(b * t) ** j
    y = np.sin(c * t) - np.sin(d * t) ** k

    plt.plot(x, y)
    plt.xlabel("eje x")
    plt.ylabel("eje y")
    plt.show()


# No modificar a partir de esta línea
if __name__ == '__main__':
    dibuja_curva([2, 3, 2, 3, 1, 3], [0, 10], 10000)
