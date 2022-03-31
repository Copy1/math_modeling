 #сердце
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
heart, = plt.plot([], [], 'o', color='red')

xdata, ydata = [], []

def tuz(t):
 x = 16 * np.sin(t)**3
 y = 13 * (np.cos(t)) - 5 * (np.cos(2*t)) - 2 * (np.cos(3*t)) - (np.cos(4*t))
 return x, y

edge = 20
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

coordsx = []
coordsy = []
t  = np.linspace(0,2*np.pi, 500)
for i in range(len(t)):
  coordsx.append(tuz(t=t[i])[0])
  coordsy.append(tuz(t=t[i])[1])

def animate(i):
  heart.set_data(coordsx[:i], coordsy[:i])

ani = FuncAnimation(fig,
                   animate,
                   frames = len(coordsx),
                   interval = 30
                   )
ani.save ('lab_7_heart.gif')

