# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 09:44:08 2022

@author: APELLIDOS, NOMBRE (DNI)

Tipo de problema: Suma de senoides, plot

Cualquier señal periódica puede aproximarse por una suma de senoides.
Esto resulta muy útil para analizar y describir muchos fenómenos físicos.

El presente programa ilustra gráficamente cómo se puede aproximar una onda
cuadrada de periodo 2*pi por una suma de senoides, en la forma:

v(t, N) = sin(t)/1 + sin(3*t)/3 + sin(5*t)/5 + sin(7*t)/7 + ... + sin(N*t)/N

Nota: una onda cuadrada es una señal periódica que alterna entre dos valores alto->bajo->alto...
a lo largo del tiempo:

  * * * *     * * * *     * * * *
  *     *     *     *     *     *
  *     *     *     *     *     *
* *     * * * *     * * * *     * *

Se pide programar tres funciones:

1) Función calcula_suma_senoides(t, N):
    Recibe como argumentos:
    t: la abscisa en la que se calcula la onda cuadrada (float)
    N:  el número de términos utilizados para la aproximación (int)

    Devuelve el valor de la aproximación v(t, N)

2) Función onda_cuadrada(N, intervalo, n_puntos):
    Recibe como argumentos:
    N:  el número de términos utilizados para la aproximación (int)
    intervalo: [t_ini, t_fin] valores inicial y final de las abscisas
    n_puntos: número de abscisas a utilizar en el intervalo

    Devuelve dos listas:
        lista_t: con los n_puntos valores de tiempos equiespaciados en el
                 intervalo [t_ini, t_fin]
        onda:    con n_puntos valores correspondientes a los valores v(t, N)
                 (calculados usando calcula_suma_senoides(t, N)).

3) Función dibuja_ondas(lista_N, intervalo, n_puntos):
    Recibe como argumentos:
    lista_N: Una lista con los diferentes valores de N que se van a utilizar
             para aproximar la onda cuadrada
    intervalo: [t_ini, t_fin] valores inicial y final de las abscisas
    n_puntos: número de abscisas a utilizar en el intervalo

    Usando un bucle irá generando las ondas cuadradas (llamando a la función
    onda_cuadrada()) y dibujándolas para cada uno de los valores en lista_N
    El título de la gráfica será 'Aproximaciones a onda cuadrada'

"""

import matplotlib.pyplot as plt
import numpy as np


def calcula_suma_senoides(t, N):
    pass  # Sustituya pass por su solución


def onda_cuadrada(N, intervalo, n_puntos):
    pass  # Sustituya pass por su solución


def dibuja_ondas(lista_N, intervalo, n_puntos):
    pass  # Sustituya pass por su solución
    
    
    
# No modificar el código a partir de aquí (salvo para pruebas)
if __name__ == "__main__":
    dibuja_ondas([3, 9, 200], [0., 10.], 1000)
    # Puedes ver en el fichero ej2_figura.png la salida esperada