while True:

    numero = int(input("Escribe un número entero: "))
    
    if numero == 0:
        break
    
    numeroReverso = 0
    digitosMayor5 = 0
    
    signo = 1 if numero >= 0 else -1
    
    numero = abs(numero)
    
    while numero > 0:
        digito = numero % 10
        
        numeroReverso = numeroReverso * 10 + digito
        
        if digito > 5:
            digitosMayor5 += 1
        
        numero = numero // 10
    
    numeroReverso = signo * numeroReverso
    
    print(f"Número al revés: {numeroReverso}")
    print(f"Dígitos mayores a 5: {digitosMayor5}")