# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:37:18 2022

@author: APELLIDOS, NOMBRE (DNI)
"""
'''
***********************************************************************************************
Tipo de problema: Procesar una lista

El módulo de un vector es la raiz cuadrada del sumatorio de sus elementos
elevados al cuadrado.
Normalizar un vector consiste en dividir los elementos del vector por su módulo.

Escribe una función normaliza() que:
    1. Recibe una lista v con las componentes de un vector a normalizar:
        [v_0, v_1, ..., v_n]  (v_i int o float indistintamente)
    2. Cacula el módulo del vector (raíz cuadrada de la suma de los cuadrados
        de sus componentes v_i). Por simplicidad, supondremos esta suma != 0.
    3. Devuelve una lista w con las componentes del vector v normalizadas:
        [w_0, w_1, ..., w_n]   (w_i = v_i / modulo)

Ej: Para v = [3, 0, 5, -4] devolvería w = [0.424, 0.0, 0.707, -0.565]
***********************************************************************************************
'''

'''
Puntuación del ejercicio: 4 sobre 100
'''

from math import sqrt


def normaliza(v):

    return w



# No modificar el código a partir de aquí
if __name__ == '__main__':
    v = [3, 0, 5, -4]
    w = normaliza(v)
    print(f"Vector original:\n\t{v}")
    print(f"Vector normalizado:\n\t{w}")