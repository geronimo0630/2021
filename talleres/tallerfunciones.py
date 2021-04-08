#punto 1 
def mostrarLista (lista):
    for elemento in lista :
        print (elemento)

edad = [10,12,15,17,18,20,21,99]
nombres = ['geronimo','daniel','tomas','andres','gerardo']
mostrarLista(edad)
mostrarLista(nombres)

#punto 2
def infolista (lista):
    mayor = max (lista)
    menor = min (lista)
    acumulador = 0
    for elemento in lista:
        acumulador += elemento
    tamañoLista = len (lista)
    promedio = acumulador / tamañoLista
    print (f'el numero mayor de la lista es el {mayor},el numero menor de la lista es {menor} y el promedio {promedio}')
edad = [10,12,15,17,18,20,21,99]
infolista(edad)

#punto 3 
def saludar (cantidad = 0):
    print ('whats up bro!!!'* cantidad)
saludar (4)

#punto 4
def pareslista (lista):
    pares = []
    for elemento in lista :
        if elemento % 2==0:
            pares.append (elemento)
    return pares
edad = [10,12,15,17,18,20,21,99]
edades_pares = pareslista ( edad)
print (edades_pares)

#punto 5
def mayoreslista(lista):
    mayores = []
    for elemento in lista:
        if elemento > 24:
            mayores.append(elemento)
    return mayores
edad = [10,12,15,17,18,20,21,99]
edades_mayores = mayoreslista(edad)
print (edades_mayores)

#punto 6
def calcularIMC (peso,altura):
    return peso/(altura**2)
IMC = calcularIMC (78,1.85)
print (IMC)

#punto 7
def despedida ():
    print ('espero sacar un 5 en el taller XD XD XD')
despedida ()