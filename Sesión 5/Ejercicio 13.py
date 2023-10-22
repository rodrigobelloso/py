num1 = int(input("Escribe el primer número: "))
num2 = int(input("Escribe el segundo número: "))

absolNum1 = abs(num1)
absolNum2 = abs(num2)

resultado = 0

for i in range(absolNum2):
    resultado += absolNum1

if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
    resultado = -resultado

print("El producto de {} y {} es: {}".format(num1, num2, resultado))