import matplotlib.pyplot as plt
meses = ['enero','feb','marzo','abril','mayo','junio','julio','agosto','sep','oct','nov','dic']
ingresos = [987,567,897,456,999,879,897,956,342,550,342,888]
plt.bar(meses,ingresos,width=0.6,color='b')
plt.title('ingresos anuales de trabajador independiente')
plt.xlabel('meses')
plt.ylabel('ingresos X1000 en pesos')
plt.show()
