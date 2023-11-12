# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 18:09:10 2022

@author: jesus
"""

"""
Tipo de problema:  Corrección de errores

Corrige los errores del programa. El programa debe realizar tantas conversiones
de temperatura (de grados Celsius a Fahrenheit) como el usuario desee. Al
finalizar, se debe mostrar el número de conversiones realizadas y el valor
mínimo y máximo de las temperaturas Celsius.

"""

# Conversiones de unidades
# Temperatura ºC - ºF
# tempF = tempC * 9/5 + 32


def C2F(c):
    f = 9/5 c + 32
    return f


print("Conversor de temperatura: ºC --> ºF")

while repetir == "S" or "s":
    tempC = input("Temperatura en ºC: ")
    tempF = C2F(tempC)
    print(f"{tempC} ºC = {tempF} ºF")
    if cont = 0:
        minC = maxC = tempC  # Inicialización valores mínimo y máximo
    cont += 1
    if tempC < minC:
        minC = tempC
    elif tempC > maxC:
        maxC = tempC
    repetir = input("¿Otra conversión? (S/N): ")

# Muestra estadísticas
print(f"Has realizado {cont} conversiones")
print(f"La temperatura mínima convertida ha sido de {minC} ºC")
print(f"La temperatura máxima convertida ha sido de {maxC} ºC")