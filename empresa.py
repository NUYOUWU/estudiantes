empleados_entre_1_y_3_millones = 0
empleados_mas_de_3_millones = 0
gasto_total_sueldos = 0

num_empleados = int(input("Ingrese el número de empleados en la empresa: "))

for i in range(num_empleados):
    sueldo = float(input(f"Ingrese el sueldo del empleado {i + 1}: $"))
    gasto_total_sueldos += sueldo
    if 1000000 <= sueldo <= 3000000:
        empleados_entre_1_y_3_millones += 1
    elif sueldo > 3000000:
        empleados_mas_de_3_millones += 1

print("Cantidad de empleados que cobran entre $1,000,000 y $3,000,000:", empleados_entre_1_y_3_millones)
print("Cantidad de empleados que cobran más de $3,000,000:", empleados_mas_de_3_millones)
print("Gasto total en sueldos para el personal:", gasto_total_sueldos)
