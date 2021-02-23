mensaje_distancia = "ingrese distancia en centimetros: "
pregunta_unidad = "en que unidad deseas ponerlo:"




mensaje_error = "entrada no vlaida"

distancia = float (input(mensaje_distancia))
unidad = (input(pregunta_unidad))


km = distancia *10**-5
metros = distancia *10**-2
mm = distancia*10

if (unidad== "km"):
    print (km)
elif (unidad == "metros"):
    print (metros)
elif (unidad == "mm"):
    print (mm)
else :
    print (mensaje_error)



