import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

x = 0.0
y = 0.0
fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='black', label='ball')
ball2, = plt.plot([], [], 'o', color='black', label='ball')
ball3, = plt.plot([], [], 'o', color='black', label='ball')

plt.plot(x, y, color='black', marker='o')

def circle_move(R):
  alpha = np.arange(0, 2*np.pi, 0.01)
  x = R * np.cos(alpha)
  y = R * np.sin(alpha)
  return x, y
  time.sleep(3)

def circle_func(R):
  alpha = np.arange(0, 2*np.pi, 0.01)
  x = R * np.cos(alpha)
  y = R * np.sin(alpha)
  return x, y
  time.sleep(1)

def circle(R):
  alpha = np.arange(0, 2*np.pi, 0.01)
  x = R * np.cos(alpha)
  y = R * np.sin(alpha)
  return x, y
  time.sleep(2)

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)


def animate(i):
  ball.set_data(circle_move(R=2)
  ball2.set_data(circle_func(R=1)
  ball3.set_data(circle(R=1.5),)

ani = FuncAnimation(fig,
                    animate,
                    frames=np.arange(0, 5, 0.01),
                    interval=10
                    )

ani.save('pro1_animation.gif')

