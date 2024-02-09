n = int(input("ingrese el # de empleados"))
cont = 0
cont1 = 0
gastos = 0     
for ini in range(n):
    sueldo = float(input("ingresar el valor sueldo de{ini}empleado", ini))
    gasto = gasto+sueldo
if sueldo >=1300000 and sueldo <=3000000:
    cont +=1
elif sueldo > 3000000:
    cont +=1
print("los gastos de la empresa total",gasto)
print("empleados que ganan mas entre 1.300.000 y 300.000 son:", cont)
print("emleados que ganan mas de 3.000.000 son:", cont1)
