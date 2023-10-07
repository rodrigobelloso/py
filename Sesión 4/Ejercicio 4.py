def calcular_producto_escalar(v, w):
    if len(v) != len(w):
        return None  # Error si los vectores tienen longitudes diferentes
    producto = sum(v[i] * w[i] for i in range(len(v)))
    return producto

while True:
    try:
        # Solicitar el tamaño de los vectores
        n = int(input("Ingrese el tamaño de los vectores (entero positivo): "))
        if n <= 0:
            print("El tamaño debe ser un entero positivo.")
            continue
        
        # Introducir los valores del vector v
        v = []
        print("Introduzca los valores del vector v:")
        for i in range(n):
            valor = float(input(f"v[{i}]: "))
            v.append(valor)
        
        # Introducir los valores del vector w
        w = []
        print("Introduzca los valores del vector w:")
        for i in range(n):
            valor = float(input(f"w[{i}]: "))
            w.append(valor)
        
        # Mostrar los vectores introducidos
        print("Vector v:", v)
        print("Vector w:", w)
        
        # Calcular el producto escalar
        producto_escalar = calcular_producto_escalar(v, w)
        if producto_escalar is not None:
            print("El producto escalar de v y w es:", producto_escalar)
        else:
            print("Error: Los vectores deben tener la misma longitud.")
        
        # Preguntar si se desea realizar otro producto escalar
        respuesta = input("¿Desea realizar otro producto escalar? (s/n): ")
        if respuesta.lower() != 's':
            break
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")
