#---- entradas ----#
MENSAJE_BIENVENIDA = "AVERIGUAREMOS SI ERES MAYOR DE EDAD"
MENSAJE_MAYYOR_EDAD = "eres mayor de edad"
MENSAJE_MENOR_DE_EDAD = "eres menor de edad no puedes seguir "
PREGUNTA_EDAD = "cuantos años tienes "

#----entrada al codigo----#
print (MENSAJE_BIENVENIDA)
edad = int (input (PREGUNTA_EDAD))
ismayor = edad >= 18
resultado = ""
if (ismayor):
    resultado = MENSAJE_MAYYOR_EDAD
else :
    resultado = MENSAJE_MENOR_DE_EDAD

print (resultado)

