import pandas as pd
ecgData = pd.read_csv('ppg.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
print(ecgData)
muestras = list(ecgData['muestra'].values())
voltaje = list(ecgData['valor'].values())
import matplotlib.pyplot as plt
plt.plot(muestras,voltaje)
plt.title('fotoplestimografia')
plt.xlabel('tiempo en seg')
plt.ylabel('voltaje en mv')
plt.show()