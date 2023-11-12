# -*- coding: utf-8 -*-
"""
Realizar un programa que calcule la raíz cuadrada entera de un número entero introducido
por el usuario. El programa guardará el "histórico" de la ejecución del programa en dos listas:
    - una con la lista de valores introducidos
    - otra con sus raices cuadradas

Se define la raíz cuadrada entera de un número entero n como el mayor número entero cuyo cuadrado
es menor o igual que n.

Ejemplo: la raíz cuadrada entera de 55 es 7: 7**2 = 49 < 55, mientras que 8**2 = 64 > 55


Para ello se pide:

Escribir una función raiz_cuadrada_entera() que:
    * Recibe:
        El valor entero n del que se quiere calcular su raiz cuadrada entera
    * Si n < 0, se lanzará un mensaje de error y se devolverá None
    * Calcula la raiz cuadrada entera. Sugerencia: probar 0, 1, 2, etc.
    * Devuelve:
        La raiz cuadrada entera

Escribir una función main() que:
    1. Solicita un valor entero
    2. Calcula su raiz cuadrada entera y muestra el resultado si es válido
    3. Pregunta al usuario si desea realizar otro cálculo, volviendo en su caso al punto 1.
    4. Muestra dos listas con los valores y los resultados:
        [valor_1, valor_2, ..., valor_n]
        [raiz_1, raiz_2, ..., raiz_n]
       incluido la eventual presencia de valores negativos que tendrán asociado en la
       lista de resultados None

Ejemplo de ejecución cuyo formato deberá seguirse ¡¡OBLIGATORIAMENTE!!:

    Introduce un entero no negativo: 0
    La raiz cuadrada entera de 0 es 0
    
    Si desea salir pulse 0: 1
    Introduce un entero no negativo: -4
    ERROR: El valor introducido es negativo
    
    Si desea salir pulse 0: 1
    Introduce un entero no negativo: 34
    La raiz cuadrada entera de 34 es 5
    
    Si desea salir pulse 0: 0
    El histórico de valores y resultados es:
    [0, -4, 34]
    [0, None, 5]

IMPORTANTE: No se puede hacer uso ni de la función sqrt ni ninguna otra función de biblioteca matemática.

"""

# Debes completar el código de las funciones sustituyendo pass, añadiendo en su caso,
# los parámetros que sean necesarios


def raiz_cuadrada_entera(n):  # 5 Pto
     if n < 0:
         print("ERROR: El valor introducido es negativo.")
         return None
     
     cont = 0
     while cont*cont <= n:
         cont += 1
     return cont - 1


def main():  # 5 Pto
    lista_v = []
    lista_r = []
    opcion = 1
    
    while opcion == 1:
        valor = int(input("Introduce un entero no negativo: "))
        lista_v.append(valor)
        raiz = raiz_cuadrada_entera(valor)
        lista_r.append(raiz)
        
        if raiz is not None:
            print(f"La raiz cuadrada entera de {valor} es {raiz}")
            
        opcion = int(input("Para repetir pulse el 1: "))
   
    print(f"El histórico de valores y resultados es:")
    print(lista_v)
    print(lista_r)

if __name__ == '__main__':
    main()