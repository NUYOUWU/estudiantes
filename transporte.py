nombres=[]
kilometros=[]
totalkms=[]
mb=0
b=0



for x in range(1,4):
    nom = input(f"por favor ingresar el nombre del conductor{x} :")
    nombres.append(nom)
    no = int(input(f"por favor ingresar los quilometros {x} :"))
    kilometros.append(no)
    
    for y in range(len(nombres)):
        print(nombres[y])
        print(kilometros[y])

        if kilometros[y]>=8:   
            Num1 = int(input("Ingresar los quilometros recorridos"))
            Num2 = int(input("Ingresar los quilometros recorridos"))
            sumar = Num1+Num2
            b+=1
            totalkms.append(kilometros[y])
        else:
            if kilometros[y]>=4:
                print("alumno bueno")
                b+=1



