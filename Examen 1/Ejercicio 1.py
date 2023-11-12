# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:36:42 2022

@author: APELLIDOS, NOMBRE (DNI)

Tipo de problema: Introducción de datos exigiendo alguna condición

PROBLEMA:
Un alumno ha decidido crear una aplicación informática para introducir las
notas de sus asignaturas.

Se pide implementar el código que le permita:
1.  Introducir el número de asignaturas que tiene.
     * Se debe exigir que este número sea mayor que 0. En caso de que no lo sea,
       debe mostrar un mensaje de error y volverlo a solicitar (tantas veces
       como sea necesario).
2.	Introducir la nota de cada una de las asignaturas, que pertenecerán al
    intervalo [0,10].
     * En caso de que no la nota no esté en dicho intervalo, debe mostrar un
       mensaje de error y volver a solicitar la nota (tantas veces como sea
       necesario).
     * Las notas se irán almacenando en una lista.

Ejemplo de ejecución:

    Introduzca el número de asignaturas: -1
    ERROR: El número de asignaturas debe ser positivo.
    Introduzca el número de asignaturas: 3

    Introduzca la nota de la asignatura ([0, 10]): 1.5
    Introduzca la nota de la asignatura ([0, 10]): 10.1
    ERROR: La nota 10.1 no pertenece al intervalo [0,10]
    Introduzca la nota de la asignatura ([0, 10]): 9.1
    Introduzca la nota de la asignatura ([0, 10]): 7.3

    Se introdujeron las notas de 3 asignaturas con valores [1.5, 9.1, 7.3]

"""
'''
Puntuación del ejercicio: 4 sobre 100
'''

repetir = True

while repetir:
  numAsign = int(input("Introduzca el número de asignaturas: "))

  if numAsign <= 0:
    print("ERROR: El número de asignaturas debe ser positivo.")
    
  else:
    repetir = False
    break
  
listAsign = []
notAsign = 0

for i in range(numAsign):
  while notAsign < 0:
    notAsign = int(input(f"Introduzca la nota de la asignatura {len(listAsign + 1)} de {numAsign} ([0, 10]): "))

    if notAsign < 0:
      print(f"ERROR: La nota {notAsign} no pertenece al intervalo [0,10]")
    else:
      listAsign.append(notAsign)