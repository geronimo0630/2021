#_condiciones_
MENSAJE_BIENVENIDA = "diligencia la siguiente informacion: "
mensaje_digite_dad = "ponga la edad mijjo"
mensaje_menor = "usted es menor de edad pa: "
mensaje_mayor = "puede rumbear perra"
mensaje_adulto = "ya estas cuchito"
mensaje_adulto_mayor = "ya estas todo un vejete"

#----condiciones----
print (MENSAJE_BIENVENIDA)
edad = int (input(mensaje_digite_dad))
ismenor = edad < 18
ismayor = edad >= 18 and edad <= 25
isadulto = edad >= 26 and edad <= 60 
isadultomayor = edad >= 60 

if (ismenor):
    print (mensaje_menor)
elif (ismayor):
    print (mensaje_mayor)
elif (isadulto):
    print (mensaje_adulto)

else :
    print (mensaje_adulto_mayor)


