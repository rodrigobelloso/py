# Solicitud de datos
a = float(input("Introduce a: "))
b = float(input("Introduce b: "))

# Cálculos
if a > b:
    res = a / (b*b)
else: 
    res = b / a**2

# Resultado
print("El resultado es:", res)