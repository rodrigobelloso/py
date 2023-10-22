fis = False

while not fis:
    inf = float(input("Inf: "))
    sup = float(input("Sup: "))
    if inf >= sup or inf < 0:
        print("valores no validos")
    else:
        fis = True
        
nRec = int(input("Numero de rectángulos (20 minimo)"))
if nRec < 20:
    nRec = 20
    
base = (sup-inf)/nRec
ac = 0
for i in range(nRec):
    x = inf + i* base
    ac += base*x *x
    
print("La integral calculada es: ", ac)
print("Precision respecto a la integral analítica: ", (sup**3 - inf**3)/3 - ac)