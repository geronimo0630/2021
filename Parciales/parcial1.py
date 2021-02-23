#---condiciones---#
ingrese_trigli = "ingrese el nivel del trigliceridos: "
ingrese_homo = "ingrese el nivel de homocisteina: "

mensaje_binevenida = "hola muy buenos dias!"
mensaje_op = "esta en estado optimo"
mensaje_sob = "esta en estado sobre el limite optimo"
mensaje_alto = "esta en estado alto "
mensaje_muy = " esta en estado muy alto"
MENSAJE_DESPEDIDAD = "gracias por colaborarnos. "
mensaje_trigli = "de trigliceridos "
mensaje_homo = " de homocisteina "
#---codigo---#
print (mensaje_binevenida)
trigliceridos = int (input(ingrese_trigli))
homocisteina = int (input(ingrese_homo))
isoptimo = trigliceridos < 150
issobre = trigliceridos >150 and trigliceridos < 200
isalto = trigliceridos >=200 and trigliceridos < 500
ismuy = trigliceridos >= 500
isoptimohomo = homocisteina  >= 2 and homocisteina < 15
issobrehomo = homocisteina >= 15 and homocisteina < 30
isaltohomo = homocisteina >= 30 and homocisteina < 100
ismuyhomo = homocisteina > 100
#----condicionales-----#
if (isoptimo):
    print (mensaje_op,mensaje_trigli)
elif (issobre):
    print (mensaje_sob,mensaje_trigli)
elif (isalto):
    print (mensaje_alto,mensaje_trigli)
else:
    print (mensaje_muy,mensaje_trigli)
#-----condicionales homocisteina-----#

if (isoptimohomo):
    print(mensaje_op,mensaje_homo)
elif (issobrehomo):
    print (mensaje_sob,mensaje_homo)
elif (isaltohomo):
    print (mensaje_alto,mensaje_homo)
else:
    print (mensaje_muy,mensaje_homo)

print (MENSAJE_DESPEDIDAD)

