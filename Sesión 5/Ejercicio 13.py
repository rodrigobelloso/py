# Solicita al usuario ingresar dos números enteros
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

# Calcula el valor absoluto de ambos números
abs_num1 = abs(num1)
abs_num2 = abs(num2)

# Inicializa el resultado en 0
resultado = 0

# Realiza el producto de los valores absolutos mediante sumas sucesivas
for _ in range(abs_num2):
    resultado += abs_num1

# Determina el signo del resultado
if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
    resultado = -resultado

# Muestra el resultado
print(f"El producto de {num1} y {num2} es: {resultado}")
