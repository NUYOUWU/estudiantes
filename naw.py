nombre []
dia =0
dias=['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
kms=[]
toal1=[]
kmscond=[]
totalkms=0
kmscond=0
nomcond=int(input("ingrese cuantos conductores tiene"))
for x in range(nomcond):
    nom = input(f"ingrese  el nombre del conductor {x+1}:")
    nombre.append(nom)
    totalkms=0
    for dia in dias:
        kms = int(input(f"ingrese los quilometros transcurridos:{dia}"))
        
toal1.append(totalkms)
totalkms+=kms
for nombre,totalkms in zip(nombre,totalkms):
    rpint(f"{nombre}:{totalkms}kilometros")
