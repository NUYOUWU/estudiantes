persona = {
    "nombre":"nuyo auki",
    "apellido":"vargas forero",
    "estatura":1.50,
    "edad":50,
    "email":"navargasf98@gmail.com",
    "ciudadnac":"beigin",
    "genero":["masculino","femenino","otro"]
}
print(persona)
#mostrar elementoo de un diccionario
print(f"le nombre de la persona es",{persona["nombre"]})
#agregar elemento a diccionario
persona["telefono"]=3218891534
print (persona)
#modificar elemento del diccionario
persona ["telefono"]=3209341575
print (persona)
#modificar la clave
persona["celular"]=persona.pop("telefono")
print(persona)
#eliminar un elemento del diciionario
del persona["celular"]
print(persona)

#iterar los items de las claves y valores
for clave,valor in persona.items():
    print(clave, ":",valor)