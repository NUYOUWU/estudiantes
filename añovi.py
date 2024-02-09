año = int(input("ingrese un año"))
if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0: 
    print("el año", año, "es biciesto")
else:
    print("el año", año, "no es biciesto")