"""
Created on Wed Dec  7 17:49:24 2022

@author: APELLIDOS, NOMBRE (DNI)
    
Se ha exportado la información de una base de datos a un fichero de texto
llamado “inventario.txt” en el que consta el inventario de una empresa de papelería
que posee varios almacenes. 

Cada registro contiene:
    el nombre del producto (tipo string)
    el número de almacén donde está almacenado (tipo int)
    el número de unidades o stock del producto (tipo int)
    el precio por unidad (tipo float).

Ejemplo de parte del contenido del fichero “inventario.txt”:
    
LAPICERO_NEGRO_HB	1	24	0.49
SACAPUNTAS_SIMPLE	2	45	0.99
GOMA_LAPIZ			3	22	0.39
GOMA_BOLIGRAFO		3	24	0.89
…

Es decir, la primera línea nos indica que:
    tenemos en inventario un producto que se trata de un LAPICERO_NEGRO_HB,
    que se encuentra en el almacén 1,
    que disponemos de 24 unidades de este producto y
    que su precio unitario es 0.49€.

Misma interpretación para el resto de las líneas (se muestran solo 4 pero puede
haber muchas más).

Funciones a programar:
1) Debe programar una función denominada pide_almacen() que se encargue de
   solicitar el número de almacén y devuelva un valor válido: {0, 1, 2, 3}.

2) Debe programar una función denominada valora_y_muestra_almacen(n_almacen), que
   recibe como argumento el número de almacén y realiza las siguientes acciones:
       Lee el fichero “inventario.txt”
       Muestra los tipos de productos que contiene el almacén n_almacen y el
       número de ellos (si no tiene unidades de un producto este no se muestra).
       Muestra el valor total de los productos almacenados en el almacén.


El programa principal deberá:
3) Solicitar el número de almacén mediante la función pide_almacen(). Si se
   devuelve 0 finalizará el programa
4) Si el número de almacén no es 0 mostrará la información del almacén usando
   valora_y_muestra_almacen()
5) Volver al paso 1)

Ejemplo de ejecución:

    Dame el número de almacen ([1-3] o 0 para salir): 1
    LAPICERO_NEGRO_HB --> 24
    SACAPUNTAS_DOBLE --> 24
    CUADERNO_ESPIRAL_A4 --> 45
    CAJA_ROTULADORES --> 24
    CAJA_ACUARELAS --> 22
    El valor del almacen 1 es 373.21 euros


    Dame el número de almacen ([1-3] o 0 para salir): 2
    SACAPUNTAS_SIMPLE --> 45
    LAPICERO_NEGRO --> 45
    BOLIGRAFO_ROJO --> 45
    PINCEL --> 45
    El valor del almacen 2 es 148.05 euros


    Dame el número de almacen ([1-3] o 0 para salir): 3
    GOMA_LAPIZ --> 22
    GOMA_BOLIGRAFO --> 24
    BOLIGRAFO_NEGRO --> 22
    BOLIGRAFO_VERDE --> 24
    CUADERNO_ESPIRAL_FOLIO --> 22
    El valor del almacen 3 es 124.28 euros


    Dame el número de almacen ([1-3] o 0 para salir): 0
    FIN PROGRAMA

"""


def valora_y_muestra_almacen(n_almacen):
    pass  # Sustituya pass por su solución


def pide_almacen():
    pass  # Sustituya pass por su solución

# Programa principal. Introduzca su código
