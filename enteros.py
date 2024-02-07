cont = 0
acum = 0
while cont < 10:
    num = int(input("Ingrese el número: "))
    acum += num
    cont += 1

promedio = acum / 10

print("La suma de los números es:", acum)
print("El promedio de los 10 números es:", promedio)