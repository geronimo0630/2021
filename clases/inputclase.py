#-------constantes-------#
PREGUNTA_NOMBRE = "como te llamas? : "
PREGUNTA_EDAD = " cuantos años tienes? : "
PREGUNTA_ESTATURA = "cuanto mides ? : "

MENSAJE_SALUDO = "un gusto conocerte"
ESTAS_GANDE = "uy estas grande nea"


#----- entrada al codigo ------#
nombre = input (PREGUNTA_NOMBRE)
print (MENSAJE_SALUDO,nombre)
edad = int (input (PREGUNTA_EDAD))
estatura = float (input (PREGUNTA_ESTATURA))
print (edad,estatura)
print (ESTAS_GANDE)

