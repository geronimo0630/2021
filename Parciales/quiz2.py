temperatura_corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
#--preguntas---#
pregunta_Menu ='''ingrese alguna opcion
        1-Convertir temperaturas
        2- desea saber si su temperatura es saludable 
        3- saber temperatura maxima o minima
        4-salir del programa 

'''

pregunta_temperatura = '''
        F- para fahrenheit
        K- para kelvin 
        C- la conversion no es necesaria
'''
#--mensajes---#
mensaje_error1 = 'escoja un letra valida entre F,K,C'
mensaje_error2 = 'escoja un numero valido entre el 1,2,3,4'

temperatura_maxima = 'La temperatura maxima es : '
temperatura_minima = 'La temperatura minima es : '


#--inicio codigo--#
opcion = int (input(pregunta_Menu))
listafaren = []
listakel = []
listaDeTemperatura = []
for elemento in temperatura_corporal:
    fahrenheit = elemento*1.8+32
    listafaren.append(fahrenheit)
for elemento in temperatura_corporal:
    kelvin = elemento+273
    listakel.append (kelvin)

#--pregunta-1-----#
while (opcion != 4):
    if (opcion==1):
        opcionTemperatura = (input(pregunta_temperatura))
        if(opcionTemperatura == 'F'):
            print(listafaren)
        elif (opcionTemperatura == 'K'):
            print(listakel)
        elif (opcionTemperatura == 'C'):
            print('no es necesaria la conversion',temperatura_corporal)
        else:
            print(mensaje_error1)
#pregunta-2
    elif (opcion==2):
        for elemento in temperatura_corporal:
            if (elemento<36):
                temperatura = 'usted tiene hipotermia'
            elif (elemento>= 36 and elemento<37.6):
                temperatura = 'usted tiene temperatura normal'
            else :
                temperatura = 'tiene fiebre'
            listaDeTemperatura.append(temperatura)

        print (listaDeTemperatura)
#pregunta-3
    elif(opcion==3):
        print (temperatura_maxima,max(temperatura_corporal))
        print (temperatura_minima,min(temperatura_corporal))
#parte 4
    else:
        print (mensaje_error2)
    opcion = int (input(pregunta_Menu))

print ('feliz día')

