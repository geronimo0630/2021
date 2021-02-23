#----condiciones---#
mensaje_binevenida = "hola que se dice pa "
mensaje_mayor = " a es mayor  "
mensaje_menor ="a es menor   "
mensaje_igual = " son igual  "

MENSAJE_A = "ingrese un numero A :"
MENSAJE_B= "ingrese un numero B: "
#----CODIGO----
print (mensaje_binevenida)
A = int (input (MENSAJE_A))
B = int (input (MENSAJE_B))
ismayor = A > B
ismenor = A < B
isigusl = A == B
resultado = ""
if (ismayor):
    print (mensaje_mayor)
elif (ismenor):
    print (mensaje_menor)
else :
    print  (mensaje_igual)

print (resultado)




