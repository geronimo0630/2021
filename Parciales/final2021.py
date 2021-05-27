#punto 1 
import matplotlib.pyplot as plt
listaalimentosfav = []
listaprecios = []
for i in range (8):
    elemento = input('ingrese 8 alimentos favoritos: ')
    listaalimentosfav.append(elemento)
for i in range (8):
    elemento = float (input('ingrese los precios de cada snack puesto: '))
    listaprecios.append(elemento)
#########
plt.bar(listaalimentosfav,listaprecios)
plt.title('alimentos favoritos')
plt.xlabel('alimentos')
plt.ylabel ('precio')
plt.savefig ('graficos alimentosfavoritos.png')
#########
plt.show()



