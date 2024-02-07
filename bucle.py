import random

secreto = random.randit (1,10)

numero = int(input("adivinar el numero entre 1 y qo"))

while numero !=secreto :
    if numero < secreto:
        print("el numero mayor")
    else:
        print("el numero menor")
        
    numero = int(input("intente de nuevo:"))

print("felicidades adivinaste el numero secreto :",secreto)
