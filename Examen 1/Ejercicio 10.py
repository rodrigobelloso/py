# -*- coding: utf-8 -*-
"""
Encuentra todos los múltiplos de un valor entero en un intervalo cerrado. Se almacenarán en una lista.

Para ello se pide:

    Escribir una función multiplos() que:
        * Recibe:
            El límite inferior entero del intervalo
            El límite superior entero del intervalo
            El divisor entero para determinar los múltiplos
        * Almacena en una lista sus múltiplos
        * Devuelve:
            La lista de múltiplos o None si inf > sup
    
    
            Escribir una función solicitaIntervaloEntero() que:
                * Solicita al usuario los límites enteros inf y sup.
                  Si inf > sup emite mensaje de error y vuelve a solicitarlos.
                * Devuelve:
                    La tupla formada por los límites

    Escribir una función main() que:
        1. Solicita el intervalo entero
        2. Solicita el divisor entero. Si es 0, se lanzará mensaje de error y finalizará el programa.
        3. Calcula la lista de múltiplos
        4. Muestra la lista con los múltiplos o mensaje de que no se encontraron

Ejemplos de ejecución cuyo formato deberá seguirse ¡¡OBLIGATORIAMENTE!!:

Ejemplo 1:
    Dame el valor inferior del intervalo: 33
    Dame el valor superior del intervalo: 3
    ERROR: No se cumple 33 <= 3
    Se volverán a solicitar los valores.
    Dame el valor inferior del intervalo: 3
    Dame el valor superior del intervalo: 33
    Dame el divisor: 34
    No se encontraron múltiplos de 34 en el intervalo [3, 33]

Ejemplo 2:
    Dame el valor inferior del intervalo: -5
    Dame el valor superior del intervalo: 25
    Dame el divisor: 5
    Los múltiplos de 5 en el intervalo [-5, 25] son [-5, 0, 5, 10, 15, 20, 25]

Ejemplo 3:
    Dame el valor inferior del intervalo: 3
    Dame el valor superior del intervalo: 33
    Dame el divisor: 0
    ERROR: introdujo 0 como divisor.
"""
# Debes completar el código de las funciones sustituyendo pass, añadiendo en su caso,
# los parámetros que sean necesarios


def multiplos(tuplaConValores, divisorEntero):  # 4 Pto

    listaMultiplos = []
    
    multInf = tuplaConValores[0]
    multSup = tuplaConValores[1]
    
    if multInf > multSup:
        return None
    else:
        for i in range(multInf, multSup + 1):
            if i % divisorEntero == 0:
                listaMultiplos.append(i)
            else:
                None
            
    return listaMultiplos
        
    
def solicitaIntervaloEntero():  # 3 Pto

    inf = 1
    sup = 0
    tuplaValores = []
    
    while not inf < sup:
        inf = int(input("Dame el valor inferior del intervalo: "))
        sup = int(input("Dame el valor superior del intervalo: "))
        
        if inf >= sup:
            print(f"ERROR: No se cumple {inf} <= {sup}")
        else:
            tuplaValores.append(inf)
            tuplaValores.append(sup)
            
    return tuplaValores


def main():  # 3 Pto

    tuplaConValores = solicitaIntervaloEntero()
    
    divisorEntero = int(input("Dame el divisor entero: "))
    
    if divisorEntero == 0:
        print(f"ERROR: Se introdujo {divisorEntero} como divisor.")
    else:
        hallarMultiplos = multiplos(tuplaConValores, divisorEntero)
        if hallarMultiplos == []:
            print(f"No se encontraron múltiplos de {divisorEntero} en el intervalo {tuplaConValores}")
        else:
            print(f"Los múltiplos de {divisorEntero} en el intervalo {tuplaConValores} son {hallarMultiplos}")
            

if __name__ == '__main__':
    main()
