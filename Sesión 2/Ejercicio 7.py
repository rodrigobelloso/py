pr1 = float(input("Introduzca el producto 1: "))
iva1 = int(input("Introduzca el IVA del producto 1: "))

pr2 = float(input("Introduzca el producto 2: "))
iva2 = int(input("Introduzca el IVA del producto 2: "))

pr3 = float(input("Introduzca el producto 3: "))
iva3 = int(input("Introduzca el IVA del producto 3: "))

suma = 0

if iva1 == 1:
    suma = suma + pr1 * 1.21
elif iva1 == 2:
    suma = suma + pr1 * 1.18
elif iva2 == 3:
    suma = suma + pr1 * 1.04
else:
    print("No se sumara el producto 1 ya que su IVA es incorrecto.")
    
if iva2 == 1:
    suma = suma + pr1 * 1.21
elif iva2 == 2:
    suma = suma + pr1 * 1.18
elif iva2 == 3:
    suma = suma + pr1 * 1.04
else:
    print("No se sumara el producto 2 ya que su IVA es incorrecto.")
    
if iva3 == 1:
    suma = suma + pr1 * 1.21
elif iva3 == 2:
    suma = suma + pr1 * 1.18
elif iva3 == 3:
    suma = suma + pr1 * 1.04
else:
    print("No se sumara el producto 3 ya que su IVA es incorrecto.")

print("El total de los productos cun su IVA es: ", suma)