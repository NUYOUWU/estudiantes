numero = int(input("Ingrese el número de personas: "))

sumaalturas = 0

for i in range(n):
    altura = float(input(f"Ingrese la altura de la persona {i+1} (en metros): "))
    sumaalturas += altura

promedioalturas = sumaalturas / numero

print("El promedio de las alturas de las personas es:", promedioalturas, "metros")
