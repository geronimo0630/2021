import matplotlib.pyplot as plt
pielabels =['mate', 'fisica ','programacion','humanidades']
sizes = [30,25,15,10]
explode = [0,0,0.1,0]
plt.pie(sizes,labels = pielabels)
###########
plt.title('materias mas perdidas por los estudiantes')
plt.show()