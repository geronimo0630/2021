##ecg1
import pandas as pd
ecgData = pd.read_csv('ecg1.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
print(ecgData)
muestras = list(ecgData['muestra'].values())
voltaje = list(ecgData['valor'].values())
import matplotlib.pyplot as plt
plt.plot(muestras,voltaje)
plt.title('electrocardiograma.png')
plt.savefig('Electrocardiograma quiz')
print('Un electrocardiograma ECG o EKG registra la señal eléctrica del corazón para buscar diferentes afecciones cardíacas. Se colocan electrodos en el pecho para registrar las señales eléctricas del corazón que provocan los latidos')
plt.show()


