import math
import matplotlib.pyplot as plt

rgMin = 1
rgMax = 25
rgF = range(rgMin, rgMax + 1)

def aproximacion_pi(n, tipo):
    if tipo == 'wallis':
        opw2 = 1
        
        for w in range(1, n + 1):
            opw1 = (4 * w ** 2) / (4 * w ** 2 - 1)
            opw2 *= opw1
            opw3 = opw2 * 2
        return opw3
        
    elif tipo == 'madhava':
        opm2 = 0
        opm3 = 0
        
        for m in range(1, n + 1):
            opm1 = (-1) ** m / (3 ** m * (2 * m + 1))
            opm2 += opm1
        opm3 += (opm2 + 1) * math.sqrt(12)
        return opm3
    
    else:
        print("ERROR: el argumento pasado no corresponde ni con wallis ni con madhava.")

def error(n, tipo):
    aprox = aproximacion_pi(n, tipo)
    errorAbsoluto = abs(aprox - math.pi)
    return errorAbsoluto

def representar(errorWallis, errorMadhava, titulo, etiquetaX, etiquetaY):
    plt.plot(rgF, errorWallis, label='wallis')
    plt.plot(rgF, errorMadhava, label='madhava')
    plt.title(titulo)
    plt.xlabel(etiquetaX)
    plt.ylabel(etiquetaY)
    plt.show()

def main():
    errorWallis = []
    errorMadhava = []
    
    tipoWallis = 'wallis'
    tipoMadhava = 'madhava'
    
    for n in rgF:
        llamadaErrorWallis = error(n, tipoWallis)
        errorWallis.append(llamadaErrorWallis)
        
        llamadaErrorMadhava = error(n, tipoMadhava)
        errorMadhava.append(llamadaErrorMadhava)
    
    representar (
        errorWallis, 
        errorMadhava,
        titulo="wallis (azul): " + str(errorWallis[-1]) + "\nmadhava (naranja): " + str(errorMadhava[-1]),
        etiquetaX="Valor de n", 
        etiquetaY="Error de π"
    )

if __name__ == "__main__":
    main()
