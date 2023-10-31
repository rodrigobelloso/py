import math

def intervalo_numeros():
    fis = False
    while not fis:
        inf = int(input("Inf: "))
        sup = int(input("Sup: "))

        if inf >= sup or inf < 0:
            print("Valores incorrectos")
        else:
            fis = True
            return inf, sup
        
print(inf)
print(sup)
