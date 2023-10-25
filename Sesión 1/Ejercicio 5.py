x1 = float(input("Coordenada X del punto 1: "))
y1 = float(input("Coordenada Y del punto 1: "))
m1 = float(input("Masa en el punto 1: "))

x2 = float(input("\nCoordenada X del punto 2: "))
y2 = float(input("Coordenada Y del punto 2: "))
m2 = float(input("Masa en el punto 2: "))

x3 = float(input("\nCoordenada X del punto 3: "))
y3 = float(input("Coordenada Y del punto 3: "))
m3 = float(input("Masa en el punto 3: "))

xg = x1 * m1 + x2 * m2 + x3 * m3
yg = y1 * m1 + y2 * m2 + y3 * m3

print("\nLas coordenadas del centro de gravedad son: (",xg,",",yg,")")