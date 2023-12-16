# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 20:08:34 2022

@author: APELLIDOS, NOMBRE (DNI)

Tipo de problema: Leer vector de fichero, cálculos sobre vectores, dibujar

Hacer un programa que calcule y dibuje la aproximación de la función
exponencial e^x mediante la serie:
    n=∞
    ∑   x^n/n!
    n=0

Se comparará visualmente la aproximación obtenida con la función exp del
módulo math utilizando una colección de abscisas (valores reales) almacenadas
en un fichero, una abscisa por línea.

Se deberán programar las siguientes funciones:
    1) Programar la función calcula_exp_aprox(x, n) que devuelva la aproximación
       e^x para n términos. Se recomienda apoyarse en la función dada factorial(n).
    2) Programar la función lee_lista_abscisas(nombre_fichero) que permite leer
       de un fichero la lista de abscisas lista_x que se usarán para la comparación

El programa principal deberá:
	3) Solicitar el número de términos n que se desean calcular de la serie.
       Si el número introducido por el usuario es menor que 5, el programa
       fijará el número de términos a 5.
    4) Solicitar el nombre del fichero que contiene las abscisas
	5) Leer del fichero la lista de abscisas usando la función lee_lista_abscisas()
	6) Obtener dos listas de ordenadas:
        6.1) La correspondiente a utilizar la función exp() de la biblioteca
             math para cada una de las abscisas en lista_x
        6.2) La correspondiente a utilizar calcula_exp_aprox(x, n) para cada
             una de las abscisas en lista_x
	7) Dibujar usando plot() del módulo matplotlib.pyplot cada una de las listas,
       en la misma gráfica, y tomando como valores de las abscisas lista_x
           plt.xlabel('x')
           plt.ylabel('y')

Ejemplo de ejecución:
       Diga el número de términos utilizados para calcular la serie: 5

       Deme el nombre del fichero: datos.txt


       La figura 'ej2_figura.png' muestra el resultado esperable si el usuario
       decide usar 5 términos en la aproximación.
"""

import matplotlib.pyplot as plt
import math


def factorial(n):
    fac = 1
    if n > 0:
        for i in range(2, n+1):
            fac *= i
    return fac


def calcula_exp_aprox(x, n):
    '''
    Parametros
    ----------
    x : float
        valor de x para el que se calcula la aproximacion
    n : int
        número de términos que se calculan en la serie

    Returns
    -------
    valor : la aproximación calculada para dicho valor de x usando n términos
    '''
    pass


def lee_lista_abscisas(nombre_fichero):
    '''
    Parametros
    ----------
    nombre_fichero : str
        Nombre del fichero donde se encuentra la lista de abscisas. Una por línea.

    Returns
    -------
    lista : lista de floats
        Lista con las abscisas

    '''
    pass


# PROGRAMA PRINCIPAL

# Secuencia de pasos 3 al 7 descritos más arriba. El alumno es libre de
# encapsular el código que considere oportuno en funciones de libre creación.
