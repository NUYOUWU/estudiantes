def calcular_promedio(notas):
    return sum(notas)/len(notas)

def main():
    num_alumnos=int(input("ingrese el numero de alumnos:"))
    registro_alumnos={}
    
for y in range(num_alumnos):
    nombre = input("ingrese el nombre del alumno:")
    
    if nombre in registro_alumnos