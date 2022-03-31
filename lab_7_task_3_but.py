#бабочка
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
but, = plt.plot([], [], 'o', color='plum')

xdata, ydata = [], []

def tuz(t):
 x = np.sin(t) * (np.e**np.cos(t)) - 2 * (np.cos(4*t)) - ((np.sin(t/12))**5)
 y = np.cos(t) * (np.e**np.cos(t)) - 2 * (np.cos(4*t)) - ((np.sin(t/12))**5)
 return x, y

edge = 10
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

coordsx = []
coordsy = []
t  = np.linspace(0,12*np.pi, 500)
for i in range(len(t)):
  coordsx.append(tuz(t=t[i])[0])
  coordsy.append(tuz(t=t[i])[1])

def animate(i):
  but.set_data(coordsx[:i], coordsy[:i])

ani = FuncAnimation(fig,
                   animate,
                   frames = len(coordsx),
                   interval = 25
                   )
ani.save ('lab_7_but.gif')







#13 * (np.cos(t)) - 5 * (np.cos(2*t)) - 2 * (np.cos(3*t)) - (np.cos(4*t))