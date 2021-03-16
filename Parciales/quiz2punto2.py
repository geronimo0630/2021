temperatura_corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
listaDeTemperatura = []
for elemento in temperatura_corporal:
    if (elemento<36):
        temperatura = 'usted tiene hipotermia'
    elif (elemento>= 36 and elemento<37.6):
        temperatura = 'usted tiene temperatura normal'
    else :
        temperatura = 'tiene fiebre'
    listaDeTemperatura.append(temperatura)

print (listaDeTemperatura)
