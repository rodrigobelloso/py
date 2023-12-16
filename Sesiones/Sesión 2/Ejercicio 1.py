a = float(input("Introduce a: "))
b = float(input("Introduce b: "))

if a > b:
    res = a / (b*b)
else: 
    res = b / a**2

print("El resultado es:", res)