n = int(input("n: "))

lista = [n]

while n > 1:
    if n % 2 == 0:
        n = n / 2
    else:
        n = n*3 +1
    lista.append(n)
    
print(f"La lista {lista} converge a 1 en {len(lista)} pasos")