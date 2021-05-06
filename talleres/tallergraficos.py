import matplotlib.pyplot as plt
pielabels =['bogota', 'medellin ','cali', 'cartagena de indias']
sizes = [30,25,15,10]
pieexplode = [0.1,0,0,0]
plt.pie(sizes,labels = pielabels,explode=pieexplode)
###########
plt.title('ciudades mas grandes de colombia')
plt.show()