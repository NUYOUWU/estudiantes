def ingrsar():
    enteros = []
    
    for x in range(5):
        numero = int(input("ingresar el numero"))
        enteros.append(numero)
    imprimir(enteros)
        
def imprimir(enteros):
    
    print("los datos de la lista son")
    for x in enteros:
        print(x)
        

imprimir("enteros")
