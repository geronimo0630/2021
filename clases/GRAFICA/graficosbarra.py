import matplotlib.pyplot as plt
lenguajes = ['py','java','dart','ts','elixir']
encuesta = [50.,10,20,10,10]
plt.bar(lenguajes,encuesta)
#########
plt.title('lenguajes mas usados')
plt.xlabel('lenguajes de programacion')
plt.ylabel ('porcentaje de uso de lengiajes')
plt.savefig ('graficos lenguaje.png')
#########
plt.show()
