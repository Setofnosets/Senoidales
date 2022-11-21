from math import sin, pi, cos
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.pyplot import figure
import numpy as np

#%matplotlib inline

def sine_wave(A: float, f: float, phi: float, t:float) -> float:
    return A*sin((2*pi*t*f) + phi)

def mensaje(M: float, f: float, phi: float, t: float) -> float:
    return M*cos((2*pi*t*f) + phi)

def modulacion_amplitud(A: float, M: float, fc: float, fm: float, phi: float, t: float) -> float:
    indice = M/A
    return (1 + mensaje(indice, fm, phi, t))*sine_wave(A, fc, phi, t)
def mostrar_grafica(x: list, y: list, title: str, fig: any, y1: list=None, y2: list=None) -> None:
    fig.suptitle(title, fontsize=16)

    ax = fig.add_axes([0,0,1,1])
    #ax.set_title(title)
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.yaxis.set_major_formatter(FormatStrFormatter('%g'))
    ax.yaxis.set_ticks(np.arange(-100, 100, 0.5))
    ax.xaxis.set_minor_locator(MultipleLocator(0.1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.1))
    ax.xaxis.grid(True, 'minor', linewidth=0.5)
    ax.yaxis.grid(True, 'minor', linewidth=0.5)
    ax.plot(x, y, 'g')
    if y1 is not None:
        ax.plot(x, y1, 'r')
    if y2 is not None:
        ax.plot(x, y2, 'b')


amp_max = 0.
x_max = 2*pi
x_min = 0
step = 0.01
x = np.arange(x_min, x_max, step)
#Señal con A = 3, f = 0.5 y fase = 0
mensaje1 = [mensaje(3,0.5,0,tiempo) for tiempo in x]
#Señal con A = 1, f = 5 y fase = 0
transmision = [sine_wave(10,20,0,tiempo) for tiempo in x]
#Señal modulada
modulada = [modulacion_amplitud(1,3,20,0.5,0,tiempo) for tiempo in x]

fig = plt.figure()
mostrar_grafica(x, mensaje1, "Mensaje", fig)
fig = plt.figure()
mostrar_grafica(x, transmision, "Señal de transmision", fig)

#Mostrar Graficas moduladas
fig = plt.figure()
mostrar_grafica(x, modulada, "Señal modulada", fig)
plt.show()