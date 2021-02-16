#----- constantes ------#
PREGUTNA_PESO = "INGRESE SU PESO EN KG:  "
PREGUNTA_ALTURA = "INGRESE SU ALTURA EN METROS:  "
MENSAJE_BIENVENIDA = " HOLA COMO ESTAS VOY A CALCULAR TU IMC"
MENSAJE_DESPEDIDAD = " TU IMC ES: "

#----- ENTRADA CODIGO----#
print (MENSAJE_BIENVENIDA)
peso = float (input (PREGUTNA_PESO))
estatura = float (input (PREGUNTA_ALTURA))
imc = peso/(estatura)**2
print (MENSAJE_DESPEDIDAD,imc)
isobeso = imc >= 30
print ("el resultado de la prueba de obesidad : ", isobeso)


