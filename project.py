import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
frames = 400 

def circle_move(R):
  alpha = np.arange(0, 2*np.pi, 0.01)
  x = R * np.cos(alpha)
  y = R * np.sin(alpha)
  return x, y

def circle_func(R, N):
  x, y = np.zeros(N), np.zeros(N)
  alpha  = np.linspace( 0,2*np.pi, N)
  for i in range(0, N, 1):
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
  return x, y 

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='green', label='ball')

edge = 20
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ball, = plt.plot([], [], 'o', color='green', label='ball')
ball2, = plt.plot([], [], 'o', color = 'b', ms  = 5)
ball3, = plt.plot([], [], color = 'r')


def animate(i):
  ball.set_data(circle_move(R = 1, t = np.linspace(0, 4*np.pi*i/frames, i)))
  ball2.set_data(circle_move(R = 1, t = 4 * np.pi*i/frames))
  ball3.set_data(circle_func(R = 1, N = 200))
  
ani = FuncAnimation(fig,
                   animate,
                   frames = frames,
                   interval = 20
                   )

plt.xlim(-7,7)
plt.ylim(-7,7)

ani.save('project_animation.gif')

