##ppg 1
import pandas as pd
ecgData = pd.read_csv('ppg 1.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
print(ecgData)
muestras = list(ecgData['muestra'].values())
voltaje = list(ecgData['valor'].values())
import matplotlib.pyplot as plt
plt.plot(muestras,voltaje)
plt.title('fotoplestimografia')
plt.xlabel('tiempo en seg')
plt.ylabel('voltaje en mv')
plt.savefig('Fotoplestimografiaquiz.png')
print ('Photoplethysmography (PPG) es una técnica óptica simple usada para descubrir cambios volumétricos en sangre en la circulación periférica. Es un bajo costo y un método no invasor que hace mediciones en la superficie de la piel. La técnica ofrece relacionado con la información valioso a nuestro sistema cardiovascular')
plt.show()