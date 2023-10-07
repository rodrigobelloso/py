n = int(input("n: "))

lista = []

na = n

while n > 0:
    resto = n % 10
    n = n//10
    lista.append(resto)
    
    lista.reverse()
    print(lista)
    
    
escap = True

for i in range (len(lista) // 2):
    if lista[i] == lista [len(lista) -1 - i]:
        print("no es capiciua")
        escap = False
        break
    
    if escap:
        print("{} Es capicua".format(na))
    else:
        print("{} No es capicua".format(na))