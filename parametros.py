texto = "buenos dias definiendo una funcion"

def mensaje():
    n1= int(input("ingresar el primer numero"))
    n2= int(input("ingrese el segundo numero"))
    calcularmayor(n1,n2)
    positivo(n1,n2)
def calcularmayor(num1,num2):
    

    if num1>num2:
        print("el primer numero es el mayor")
    elif num1==num2:
        print("son numero iguales")
    else:
        print("el segundo numero es el mayor")
        

def positivo(p1,p2):
    if p1>0 or p2>0:
        print("numeropositivo")
        
    elif p1<0 and p2<0:
        print("los numeros son negativos")
        
    else:
        print("almenos uno de los numeros no es positivo")   

mensaje()