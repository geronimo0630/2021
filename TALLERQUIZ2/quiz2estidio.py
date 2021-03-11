#---preguntas---#
preguntanumero = ''' ingrese alguna de estas opciones 
        1. hacer convercion de dolares o euros  
        2.agregue un valor a la lista de pesos 
        3.mostrar valor mas alto , mas bajo y promedio 
        4.eliminar elemento lista 
        5. salir 

'''
pregunta_moneda = '''
        C- Mostrar original en pesos colombianos 
        D- Mostrar en dolares 
        E-mostrar en euros
'''
preguntarNumero = 'ingrese un valor en COP: '
pregunta_borrar_coordenada = 'ingrese la posicion que desea eliminar: '
#--mensajes--#
mensajepesos = 'Mostrando lista originla'
mensajedolares ='mostrar lista en dolares'
mensajeseuros = 'mostrar lista en euros'
mensajeerro = 'valor ingresado no valido'

mensajeMayot = 'El numero ingresad es : '
mensajeMenor = 'el numero ingresado es : '
mensajePromedio ='el promedio es : '


listaPesoos = [20000,30000,4000,2500,1000,7600]
#conversion punto 1
listaEuros = []
for elemento in listaPesoos:
    listaEuros.append (elemento*0.00023)
listaDolares = []
for elemento in listaPesoos:
    listaDolares.append (elemento*0.00023)

opcionescogida = int (input(preguntanumero))

while (opcionescogida != 5):
    if (opcionescogida == 1):
        opcionMoneda = input(pregunta_moneda)
        if (opcionMoneda == 'C'):
            print (mensajepesos)
            print (listaPesoos)
        elif (opcionMoneda == 'D'):
            print(mensajedolares)
            print(listaDolares)
        elif (opcionMoneda == 'E'):
            print (mensajeseuros)
            print (listaEuros)
        else:
            print (mensajeerro)
    #---opcion2---#
    elif (opcionescogida == 2):
        valorIngresado = float (input(preguntarNumero))
        listaPesoos.append(valorIngresado)
        print (listaPesoos)
    #---opcion3---#
    elif (opcionescogida == 3):
        print (mensajeMayot,max(listaPesoos))
        print (mensajeMenor, min(listaPesoos))
        print (mensajePromedio,sum(listaPesoos)/len(listaPesoos))
    #---opcion4---#
    elif (opcionescogida == 4):
        print (listaPesoos)
        posicion = int (input(pregunta_borrar_coordenada))-1
        listaPesoos.pop(posicion)
        print (listaPesoos)
    #---opcion5---#
    else:
        print ('valor ingresado no valido')
    opcionescogida = int (input(preguntanumero))

print ('feliz dia!')
