#empezamos utilizando dos boolean.
prueba1 = True
prueba2 = False
#hicimos que apareciera en pantalla cada boolean puesto 
print (prueba2)
print (prueba1)
#probamos esta variable a ver si daba falso o verdadero
prueba1 = prueba2
print(prueba1)
# pusimos nuestra informacion con int, y float
edad = 19
estatura = 1.85
peso = 78
NOMBRE = "Geronimo buitrago"
# este es un codigo para que aparezca ordenando a la hora de imprimir en pantalla 
print ("#"*15,"mayorEdad","#"*15)
# se pone is para comprobar a la hora de hacer la operacion si la edad es mayor o igual a 18
isMayorEdad = edad >= 18
#imprime si es verdadero o falso segun la informacion que dimos al principio 
print (isMayorEdad)
print ("#"*15,"Bajo a la Estatura Promedio","#"*15)
#pusimos un menor a 1.70 que es la estatura promedio
isMayorEstatura = estatura < 1.70 
#imprime si es verdadero o falso segun la informacion que dimos al principio 
print (isMayorEstatura)
print ("#"*15,"Peso diferente a 84","#"*15)
#psusimos si el peso era diferente a 84
isPesoDiferente = peso != 84 
#imprime si es verdadero o falso segun la informacion que dimos al principio 
print (isPesoDiferente)
#le hicimos sabr a la maquina que el apellido era buitrago
apellido = "buitrago"
# con is preguntamos si el apellido era el que habia puesto en el principio
isApellido = apellido in NOMBRE
print ("#"*15,"Peso diferente a 84","#"*15)
#imprime si es verdadero o falso segun la informacion que dimos al principio 
print (isApellido)







