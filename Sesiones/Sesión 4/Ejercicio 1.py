num_val = int(input("Numero de valores: "))

lista = []

for i in range (num_val):
    lista.append(int(input("Lista[{}]: ".format(i))))
    
print("\nLa lista completa es: ", lista)

cont = 0

pares = []

for x in lista:
    if x % 2 == 0:
        pares.append(x)
        cont += 1
        
print("\nLa lista con números pares es: ", pares)
print("El número de números pares en la lista es:", len(pares), "\n")