#datos de lista 
listaDolares = [20000,30000,4000,2500,1000,7600]
#preguntas 
pregunta_monedad = '''Porfavor ingrese alguna opcion:
                1.Convertir dolares 
                2.mostrar categoria ingresos
                3.ver,maximo,minimo y promedio de ingresos 
                4.acabar programa
'''
pregunta_conversion = ''' Seleccione como desea convertir el dinero 
                D- dolares 
                E- euros 
                C- pesos COP 
'''
#mensajes
mensaje_opcion = 'usted escogio la opcion {}'
mensaje_salida = 'muchas gracias, feliz dia '
mensaje_dolares = 'no es necesaria la conversion, pero se muestra la lista'

#errores
mensaje_errornumero = 'elija una opcion del 1 al 4'
mensaje_errormoneda = 'elia una opcion entre C,D,E'
#inicio codigo 
opcion = int (input(pregunta_monedad))
listaPesos = []
listaEuros = []
listaClasificacion = []
#pasar a COP
for elemento in listaPesos :
    pesos = elemento * 37000
    listaPesos.append(pesos)
#pasar a EUR 
for elemento in listaEuros:
    euros = elemento * 0.84
    listaEuros.append (euros)
#estados de salud 
for elemento in listaDolares:
    if (elemento < 1000):
        print ('ingresos bajos')
    elif (elemento > 1000 and elemento < 7000):
        print ('ingresos medios')
    elif (elemento >= 7000 and elemento < 20000):
        print ('ingresos altos')
    else:
        print ('ingresos elevados')
#promedios 
mayor = max (listaDolares)
menor = min (listaDolares)
acomulador = 0 
for elemento in listaDolares:
    acomulador+=1
promedio = acomulador/len(listaDolares)

#menu 
while (opcion != 4 ):
    if (opcion==1):
        print(mensaje_opcion.format(1))
        conversion = input (pregunta_conversion)
        if (conversion == 'C'):
            print (listaPesos)
        elif (conversion == 'E'):
            print (listaEuros)
        elif (conversion == 'D'):
            print (listaDolares)
        else:
            print (mensaje_errormoneda)
    elif (opcion==2):
        print(mensaje_opcion.format(2))
        print (listaClasificacion)
    elif (opcion == 3):
        print(mensaje_opcion.format(3))
        print ('el ingreso maximo fue : ', mayor)
        print ('el ingreso minimo fue :', menor)
        print ('el ingreso en promedio fue : ', promedio)
    else:
        print (mensaje_errornumero)

opcion = int (input(pregunta_monedad))

print(mensaje_salida)