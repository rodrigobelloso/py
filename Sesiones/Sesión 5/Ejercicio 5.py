import math 

prec = 1e-6
i = 1
acserie = 0
nueter = 1

while nueter > prec:
    nueter = 1/ (i*i)
    acserie += nueter
    i += 1
    
print(acserie)
print("Convergencia a (pi**2)/6: ", (math.pi*math.pi)/6 - acserie)