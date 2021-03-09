for interacion in range (10):
    print (interacion)
print ('#'*60)
for interacion in range (10):

    print (interacion+1)
print ('#'*60)
for interacion in range (1,11):
    print (interacion)
print ('#'*60)
for interacion in range (1,11,2):
    print (interacion)

residuo = 5%4
print (residuo)
residuo = 4%4
print (residuo)
print ('#'*60)

for interacion in range (1.11):
    if (interacion % 2 == 0):
        print (interacion)
print ('#'*60)
for interacion in range (1.11):
    if (interacion % 2 != 0):
        print (interacion)
print ('#'*60)


rango= int (input('ingrese el numero maximo'))
opcion = int (input('''
         1-ver solo impares
         2-ver solo pares
         3-ver las dos clasificaciones 
         n-cualquier numero mostrar nada 

'''))
if (opcion == 1):
    for interacion in range (1,rango+1):
        if (interacion % 2 != 0):
            print (interacion)
elif(opcion == 2):
    for interacion in range (1,rango+1):
        if (interacion % 2 == 0):
            print (interacion)
elif (opcion == 3):
    for interacion in range (1,rango+1):
        if (interacion % 2 == 0):
            print (interacion, 'es numero par')
        else:
            print (interacion,'es un numero impar' )
else:
    print ('mostrar nada')


for interacion in range (1,rango+1):
    print (interacion)

