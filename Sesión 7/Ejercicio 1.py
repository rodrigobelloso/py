import matplotlib as plt
import numpy as np
import math

def factorial(n):
    acm = 1
    for i in range(1, n+1):
        acm *= i
        
    return acm

def seno_aprox(x, N):
    ac = 0
    for i in range(N+1):
        if i%2 == 0:
            ac += x**(2*i) / factorial(2*i + i)
        else:
            ac += -x**(2*i) / factorial(2*i + i)
        return ac
    
def crea_vector_abscisa():
    ff = False
    while not ff:
        tam = int(input("Tam: "))
        if tam <= 0:
            print("Tamaño debe de ser mayor que 0")
        else:
            ff = True
            
    x_ini = 1
    x_fin = 0
    while x_ini > x_fin:
        x_ini = int(input("Valor inferor del intervalo: "))
        x_fin = int(input("Valor superior del intervalo: "))
        
        if x_ini > x_fin:
            print(f"ERROR: No se cumple")
            
    return N

def dibuja_senos():
    lista_s = [0]*len()