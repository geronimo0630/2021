import matplotlib.pyplot as plt
pielabels =['estados unidos', 'rusia ','alemania', 'canada','colombia']
sizes = [40,20,18,13,9]
pieexplode = [0.1,0,0,0,0]
plt.pie(sizes,labels = pielabels,explode=pieexplode)
###########
plt.title('ciudades mas grandes de colombia')
plt.savefig('ciudades.png')
plt.show()