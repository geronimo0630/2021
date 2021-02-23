#----condiciones---#
pregunta_actual = "ingrese el año actual:  "
año_random = "ingrese un año cualquiera:  "

mensaje_final = "han pasado estos años:  "

#---codigo---#
actual = int (input (pregunta_actual))
random = int (input (año_random))
ismayor = actual > random
ismenor = actual < random
resta = actual - random
otraresta = random - actual

if (ismayor):
    print ("han pasado: ", resta)
elif (ismenor):
    print ("faltan estos años", otraresta)
