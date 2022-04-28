import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

print(f'введите х: { }')
print(f'введите y: { }')
#x = 0.0
#y = 0.0
fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='black', label='ball')
ball2, = plt.plot([], [], 'o', color='black', label='ball')
ball3, = plt.plot([], [], 'o', color='black', label='ball')
ball4, = plt.plot([], [], 'o', color='black', label='ball')

plt.plot(x, y, color='black', marker='o')


def circle_move(R):
  alpha = np.arange(0, 2*np.pi, 0.01)
  x = R * np.cos(alpha)
  y = R * np.sin(alpha)
  return x, y
  

def circle_func(R):
  alpha = np.arange(0, 2*np.pi, 0.01)
  x = R * np.cos(alpha)
  y = R * np.sin(alpha)
  return x, y

def circle_c(R):
  alpha = np.arange(0, 2*np.pi, 0.01)
  x = R * np.cos(alpha)
  y = R * np.sin(alpha)
  return x, y
  

def circle(R):
  alpha = np.arange(0, 2*np.pi, 0.01)
  x = R * np.cos(alpha)
  y = R * np.sin(alpha)
  return x, y
  

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)


def animate(i):
  ball.set_data(circle_move(R=i+1))
  ball2.set_data(circle_func(R=i))
  ball3.set_data(circle(R=i+0.5))
  ball4.set_data(circle_c(R=i+1.5))


ani = FuncAnimation(fig,
                    animate,
                    frames=np.arange(0, 5, 0.01),
                    interval=30
                    )

ani.save('pro1_animation.gif')


