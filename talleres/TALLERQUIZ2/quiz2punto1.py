listaPesos = [20000,30000,4000,2500,1000,7600]
pregunta_moneda = '''
        C- Mostrar original en pesos colombianos 
        D- Mostrar en dolares 
        E-mostrar en euros
'''
mensajepesos = 'Mostrando lista originla'
mensajedolares ='mostrar lista en dolares'
mensajeseuros = 'mostrar lista en euros'
mensajeerro = 'valor ingresado no valido'


listaEuros = []
for elemento in listaPesos:
    listaEuros.append (elemento*0.00023)
listaDolares = []
for elemento in listaPesos:
    listaDolares.append (elemento*0.00023)

opcionMoneda = input(pregunta_moneda)
if (opcionMoneda == 'C'):
    print (mensajepesos)
    print (listaPesos)
elif (opcionMoneda == 'D'):
    print(mensajedolares)
    print(listaDolares)
elif (opcionMoneda == 'E'):
    print (mensajeseuros)
    print (listaEuros)
else:
    print (mensajeerro)