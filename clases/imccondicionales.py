#----- constantes ------#
PREGUTNA_PESO = "INGRESE SU PESO EN KG:  "
PREGUNTA_ALTURA = "INGRESE SU ALTURA EN METROS:  "
MENSAJE_BIENVENIDA = " HOLA COMO ESTAS VOY A CALCULAR TU IMC"
MENSAJE_DESPEDIDAD = " TU IMC ES: "
MENSAJE_BAJO_PESO = "ESTAS FLAQUITO PA"
MENSAJE_ADECUADO = "ESTAMOS MELOS!"
MENSAJE_SOBRE_PESO = "OJO PA, PILAS!"
MENSAJE_OBESO : " F, EMPIECE A RODAR MEJOR PA"
#----- ENTRADA CODIGO-----#
print (MENSAJE_BIENVENIDA)
peso = float (input (PREGUTNA_PESO))
estatura = float (input (PREGUNTA_ALTURA))
imc = peso/(estatura)**2

isbajoPeso = imc < 18.5
isnormal = imc >= 18.5 and imc < 25
isSobrepeso = imc >= 25 and imc < 30 
resultado = ""
if (isbajoPeso):
    resultado = MENSAJE_BAJO_PESO
elif (isnormal):
    resultado = MENSAJE_ADECUADO
elif (isSobrepeso):
    resultado = MENSAJE_SOBRE_PESO
else:
    resultado = MENSAJE_OBESO

print (MENSAJE_DESPEDIDAD,imc)
print (resultado)

