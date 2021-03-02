#---entradas---#
mensaje_error = 'porfavor ingresar una opcion valida '
pregunta_menu = ''' ingrese 
        1-para mostrar los numeros del 1 al 5 
        2-para preguntar tu nombre 
        3- para mostrar el año en el que estamos 
        4 - salir 
'''
pregunta_nombre = 'ingrese nombre porfavor:  '

entrada = 1
while (entrada >= 1 and entrada <=3):
    entrada = int(input(pregunta_menu))
    if(entrada == 1):
        print(1,2,3,4,5)
    elif(entrada == 2):
        nombre = input (pregunta_nombre)
        print (f'bienvenido{nombre} a este menu emplea las otras opciones ')
    elif (entrada == 3):
        print ('estamos en el año 2021')
    elif (entrada ==4):
        print ('muchas gracias por usae el programa feliz dia ')
    else:
        entrada = 1
        print (mensaje_error)
