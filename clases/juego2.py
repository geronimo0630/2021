import random
#---entradas---#

mensaje_saludo = 'juguemos!'
pregunta_introduccion = '''
              en este juego debes acertar un numero
                  que va desde el 1 al 10!!!
             puedes intentarlo antes que se te acaben las vidas!!!
                       ingresa tu numero:
'''
pregunta_dificultad = '''
        1-facil
        2-moderado
        3-dificil
'''
pregunta_fallaste = 'fallo pa, vuelva a intentarlo: '
MENSAJE_DESPEDIDAD = 'felicidades pri'

#--codigo--#
numeroOculto = random.randint (1,10)
vidas = ''
dificultad = int (input(pregunta_dificultad))
while (dificultad !=1 and dificultad != 2 and dificultad != 3):
    print ('ingresa una opcion validad')
    dificultad= int (input(pregunta_dificultad))
if(dificultad == 1):
    print ('modo facil activado ')
    vidas = 5
elif (dificultad ==2):
    print ('modo moderado activado')
    vidas = 3
else:
    print ('modo dificil activado')
    vidas = 1

numegroIngresado = int (input(pregunta_introduccion))

while (numegroIngresado != numeroOculto and vidas>1):
    vidas -=1
    print ( 'te quedan estas vidas : ',vidas)
    numegroIngresado = int (input(pregunta_fallaste))

if (vidas>=0 and numegroIngresado == numeroOculto):
    print (MENSAJE_DESPEDIDAD)
else:
    print (pregunta_fallaste, 'el numero era el: ', numeroOculto)
