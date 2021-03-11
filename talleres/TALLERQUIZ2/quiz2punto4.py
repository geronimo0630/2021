listaPesos = [20000,30000,4000,2500,1000,7600]
pregunta_borrar_coordenada = 'ingrese la posicion que desea eliminar: '
print (listaPesos)
posicion = int (input(pregunta_borrar_coordenada))-1
listaPesos.pop(posicion)
print (listaPesos)