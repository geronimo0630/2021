nombres = []
print (type(nombres))
print (nombres)
nombres = ['santi','aleja','geronimo', 'elsa']
print (nombres)
print (nombres[2])
nombres.append ('mauricio')
print (nombres)
print (nombres[2])
edad = [18,19,20,17]
estaturas =[1.62,1.80,1.67,1.98]
#al iltimo 
print (edad[-2])
#de una posicion a otra
print (edad[0:2])
#------
print (edad[:3])
print (edad[2:])
print (edad[:])
#ordenar lista 
edad.sort()
print (edad)
edad.sort(reverse=True)
print (edad)
#numero mayor-menor lsit 
mayor = max (edad)
print (mayor)
menor = min (edad)
print (menor)
#como contamos cuantos elemntos hay 
largolistaedades = len (edad)
print (largolistaedades)
#como sumar 
sumaedades = sum (edad)
print (edad)
#promedio 
promedioEdades = sumaedades / largolistaedades
print (promedioEdades)
#eliminar un elemento 
edad.pop(2)
print (edad)
#ciclo for y las listas 
largolistaedades = len (edad)
for indice in range (largolistaedades):
    print (edad[indice])
largolistadoNombres = len (nombres)
for indice in range (largolistadoNombres):
    print (nombres[indice])

posicionesValoresPares = []
largolistaedades = len (edad)
for posicion in range (largolistaedades):
    if (edad[posicion]%2 == 0 ):
        posicionesValoresPares.append(posicion)
print(edad)
print (posicionesValoresPares)

#solo cuando nos interese mostrar lista 
posicion = 0
for edades in edad:
    print (edades)
for nombre in nombres:
    print (nombre)
    print(posicion)
    posicion +=1
