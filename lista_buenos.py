nombres=[]
notas=[]
amejor=[]
mb=0
b=0
iN=0
mnmb=nombres

for x in range(1,4):
    nom = input(f"por favor ingresar el nombre del alumno {x} :")
    nombres.append(nom)
    no = int(input(f"por favor ingresar las notas del alumnado {x} :"))
    notas.append(no)
    
for y in range(len(nombres)):
    print(nombres[y])
    print(notas[y])

if notas[y]>=8:
    print("alumno muy buenos")
    mb +=1
    amejor.append(nombres[y])
else:
    if notas[y]>=4:
        print("alumno bueno")
        b+=1
    else:
        print("alumno no aprueva la materia",nombres)
        iN +=1
eliminar=[]
for z in len(notas):
    if notas[z]>=4 and notas[z]<=7:
       ## notas.pop(z)
        ##nombres.pop(z)
        eliminar.append(z)
for d in sorted(eliminar,reverse = True):
        notas.pop[d]
        nombres.pop[d]

print("cantidad de alumnos muy buenos son:",mb)
print("los nombres de los mejores alumnos x nota son:",amejor)
print("lista de alumnos con notas entre 4 y 7")

