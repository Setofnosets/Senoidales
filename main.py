from math import sin, pi
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.pyplot import figure
import numpy as np

def sine_wave(A: float, f: float, phi: float, t:float) -> float:
    return A*sin((2*pi*t*f) + phi)

#Variable a modificar
fase = 3*pi/2



amp_max = 0.
x_max = 2*pi
x_min = 0
step = 0.01
x = np.arange(x_min, x_max, step)
y = [sine_wave(1, 1, fase, tiempo) for tiempo in x]
amp_max = y.index(max(y)) * step

#Agregar Ejes
ax = plt.figure().add_subplot(1, 1, 1)
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.yaxis.set_major_formatter(FormatStrFormatter('%g'))
ax.yaxis.set_ticks(np.arange(-100, 100, 0.5))
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))
ax.xaxis.grid(True,'minor',linewidth=0.5)
ax.yaxis.grid(True,'minor',linewidth=0.5)
plt.grid(True, linewidth=0.5, color='#e5e5e5', linestyle='-')
plt.annotate("Fase: " + str(fase), xy=(-0.2,1.1), xytext=(-0.2,1.1))

#Mostrar Grafica
plt.plot(x,y)
plt.show()