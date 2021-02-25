#----mensajes---#
mesaje_saludo = "hola buenos dias "
mensaje_ahorro = "llevas ahorrado..."
pregunta_valor_cpu = "cuanto vale el pc que deseas?: "
pregunta_cuanto_tiene = "cuanto llevas ahorrado "

#---entradas---#
print (mesaje_saludo)
valor = float (input(pregunta_valor_cpu))
ahorrado = float (input(pregunta_cuanto_tiene))

while(valor > ahorrado):
    print (mensaje_ahorro,ahorrado,"te faltan...",valor - ahorrado)
    ahorrado == ahorrado + 1000
print (valor == ahorrado)