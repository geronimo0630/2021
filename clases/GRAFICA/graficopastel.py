import matplotlib.pyplot as plt
##labels : python, java ,dart, javascript, nombres porciones torta
pielabels =['python', 'java ','dart', 'javascript']
sizes = [30,25,15,10]
explode = [0,0,0.1,0]
plt.pie(sizes,labels = pielabels)
###########
plt.title('uso de lenguajes de programacion 2021')
plt.savefig ('tortas.png')
plt.show()