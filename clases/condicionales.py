#----- constantes-----#
MENSAJE_BIENVENIDA = "Hola espero que estes bien"
MENSAJE_MAYOR = "el numero A es mayor que B"
MENSAJE_MENOR = "el numero A es menor que B"
MENSAJE_IGUAL = " A ES IGUAL B "

PREGUNTA_NUMEROA = "ingrese numero A: "
PREGUNTA_NUMEROB = "ingrese numero B: "

#---- entrada codigo-----#
print (MENSAJE_BIENVENIDA)
numeroA = int (input (PREGUNTA_NUMEROA))
numeroB = int (input (PREGUNTA_NUMEROB))
ismayor = numeroA > numeroB
ismenor = numeroA < numeroB
resultado = ""

if (ismayor):
    resultado = MENSAJE_MAYOR
elif (ismenor):
    resultado = MENSAJE_MENOR
else:
    resultado = MENSAJE_IGUAL

print (resultado)


