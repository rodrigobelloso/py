# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:19:35 2022

@author: APELLIDOS, NOMBRE (DNI)

Tipo de problema: Leer vector de fichero, cálculos sobre vectores, dibujar

Realiza un programa que realice una serie de cálculos sobre un conjunto de
notas en un fichero.
1. Solicitar el nombre del fichero donde se encuentran las notas
   (son valores enteros: {0,1,...10})
2. Leer las notas del fichero de texto (un valor entero por línea)
   (véase ejemplo ej2_notas.txt)
3. Calcular el histograma (histo) de las notas, es decir, una lista cuyos
   elementos son cuantos alumnos han sacado la nota correspondiente a ese
   índice de la lista:
       histo[4] = 5 indicaría que hay 5 alumnos con nota 4
4. Dibujar el histograma. Para dibujar el histograma, úsese la función
     bar(x, histo)    del paquete Matplotlib, donde
   x: es la lista con las 11 notas posibles e
   histo: es el histograma calculado anteriormente, número de alumnos que han
   sacado cada una de las notas.


Ejemplo de ejecución:

    Nombre del fichero: ej2_notas.txt

    (El programa dibujará una figura similar a 'ej2_figura.png',
    incluida en este proyecto, correspondiente a este conjunto de datos)

Puntuación del ejercicio: 10 sobre 100
"""
import matplotlib.pyplot as plt


nom = input('Nombre del fichero: ')
with open(nom, 'r') as fich:
    notas = []
    for linea in fich:
        notas.append(int(linea))

# Construyo histograma
h = 11*[0]  # El histograma tendrá 11 valores (notas de 0 a 10)
for i in range(11):
    h[i] = notas.count(i)

v_notas = list(range(11))
plt.bar(v_notas, h)
plt.title('Distribución de notas')
plt.xlabel('Notas')
plt.ylabel('Nº de Alumnos')
plt.show()
