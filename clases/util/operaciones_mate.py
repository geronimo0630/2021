def sumar (valor1 = 0, valor2 = 0, valor3 = 0 ):
    return valor1+valor2+valor3
def restar (valor1 = 0, valor2 = 0, valor3 = 0 ):
    return valor1-valor2-valor3
def multiplicacion (valor1 = 0, valor2 = 1, valor3 = 1):
    return valor1*valor2*valor3
def dividir (valor1 = 0, valor2 = 1, valor3 = 1 ):
    return valor1+valor2+valor3
def potencia (valor1 = 0, valor2 = 0, valor3 = 0 ):
    return valor1**valor2**valor3
print (sumar(2,4,6))
print (restar(2,4,6))
print (multiplicacion(2,4,6))
print (dividir(2,4,6))
print (potencia(2,2,2))


def areaTriangulo (base,altura):
    return base*(altura/2)
area = areaTriangulo (4,2)
print(area)
print ("-"*20)

def infolista (lista):
    mayor = max (lista)
    menor = min (lista)
    acumulador = 0
    for elemento in lista:
        acumulador += elemento
    tamañoLista = len (lista)
    promedio = acumulador / tamañoLista
    print (f'el numero maximo de la lista es el: {mayor},el numero minimo de la lista es: {menor} y el promedio es :{promedio}')
numero_enteros = [1,2,5,7,2,9,34,53,67,28,30]
infolista(numero_enteros)
print ("-"*20)