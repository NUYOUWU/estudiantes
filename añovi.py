año = int(input("ingrese un año"))
if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0: 
    print("el año", año, "es biciesto")
else:
    print("el año", año, "no es biciesto")
    


añoinicio = int(input("ingresar el año de inicio"))
añofinal = int(input("ingresar el año de finalisacion"))


def lineabiciesta(an,alt,letra):
    for i in range(an):
        for i in range(alt):
            print(letra,end=" ")
        print()
        
lineabiciesta(añoinicio,añofinal)