###punto 1
import matplotlib.pyplot as plt
listasancks = []
listaprecios = []
for i in range (5):
    elemento = input('ingrese 5 snacks favoritos: ')
    listasancks.append(elemento)
for i in range (5):
    elemento = float (input('ingrese los precios de cada snack puesto'))
    listaprecios.append(elemento)
#########
plt.bar(listasancks,listaprecios)
plt.title('Snaks favoritos')
plt.xlabel('snaks')
plt.ylabel ('precio')
plt.savefig ('graficos snacksfavoritos.png')
#########
plt.show()


