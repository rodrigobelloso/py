precioAdquisicion = float(input("Introduce el precio de adquisición del producto: "))

beneficio = (precioAdquisicion * 0.25) + precioAdquisicion
iva = beneficio * 0.21
total = beneficio + iva

print("\nEl precio total es: ", total)
print("El impuesto del producto es: ", iva)