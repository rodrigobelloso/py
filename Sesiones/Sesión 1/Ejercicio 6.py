horas = int(input("Introduce las horas: "))
minutos = int(input("Introduce los minutos: "))
segundos = int(input("Introduce los segundos: "))

total = horas * 3600 + minutos * 60 + segundos;
print("El tiempo en segundos es: ", total)

segundosTotales = int(input("\nIntroduce los segundos: "))

horas = segundosTotales // 3600
segundosRestantes = segundosTotales % 3600
minutos = segundosRestantes // 60
segundos = segundosRestantes % 60

print("Horas: ", horas)
print("Minutos: ", minutos)
print("Segundos: ", segundos)