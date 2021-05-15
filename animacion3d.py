#definicion de datos
import matplotlib.pyplot as plt
dormir = [7,8,9,11,13]
pythonjob = [7,8,9,10]
movimientonaranja = [8,9,10,12,15,17]
divisiones = [7,2,2,13]
mangorelajado = [2,1]
actividades = ['dormir','pythonjob','movimientonaranja','mangorelajado']
colores = ['red','green','blue','yellow']
#configuracion
plt.pie(divisiones, labels=actividades, colors=colores,startangle=90,
shadow=True, explode=(0.1,0,0,0), autopct='%1.1f%%')
#defenir titulo
plt.title('grafiquito:D')
#mostrar figura
plt.show()