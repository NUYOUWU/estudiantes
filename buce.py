ancho = int(input("ingresar el ancho del rectangulo"))
altura = int(input("ingresar laaltura del rectangulo"))
caract = input("ingresar el caracter a utilizar")

def dibujar(an,alt,letra):
    for i in range(an):
        for i in range(alt):
            print(letra,end=" ")
        print()
        
dibujar(ancho,altura,caract)

