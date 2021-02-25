#---entradas---#
mensaje_saludo = 'juguemos!'
pregunta_introduccion = '''
              en este juego debes acertar un numero
                  que va desde el 1 al 10!!!
             puedes intentarlo las veces que quieras!!!
                            exitos!!!
            ingresa tu numero:
'''
pregunta_fallaste = 'fallo pa, vuelva a intentarlo: '
MENSAJE_DESPEDIDAD = 'felicidades pri'

#---entrada al codigo---#
numeroOculto = 7 
vidas = 3
print (mensaje_saludo)
numegroIngresado = int (input(pregunta_introduccion))

if (numegroIngresado != numeroOculto):
    vidas -= 1


while (numeroOculto != numegroIngresado and vidas > 1):
    vidas -=1
    numegroIngresado = int (input(pregunta_fallaste))

if (vidas >= 0):
    print (pregunta_fallaste)
    print (vidas)
else: 
    print (pregunta_fallaste, 'el numero era... ', numeroOculto)
