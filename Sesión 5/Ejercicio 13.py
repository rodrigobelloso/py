# Función para calcular el producto de dos números enteros sin usar el operador *
def producto_sin_multiplicar(num1, num2):
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
    
    return resultado

# Solicita al usuario ingresar dos números enteros
num1 = int(input("Escribe el primer número entero: "))
num2 = int(input("Escribe el segundo número entero: "))

# Calcula el producto sin usar el operador *
resultado = producto_sin_multiplicar(num1, num2)

# Muestra el resultado
print(f"El producto de {num1} y {num2} es: {resultado}")
