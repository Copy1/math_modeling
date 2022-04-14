import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
frames = 400
def astroid(R, t):
 x = R * np.cos(t)**3
 y = R * np.sin(t)**3
 return x, y 

def circle_func(R, N):
  x, y = np.zeros(N), np.zeros(N)
  alpha  = np.linspace( 0,2*np.pi, N)
  for i in range(0, N, 1):
    x[i] = R * np.cos(alpha[i])
    y[i] = R * np.sin(alpha[i])
  return x, y 

def astroid_func(R, N, t):
  alpha = np.arange(0, 2*np.pi, 0.1)
  x = R * np.cos(t) + R * np.cos(alpha)
  y = R * np.sin(t) + R * np.sin(alpha)
  return x, y

fig, ax = plt.subplots()
fig = plt.figure()

edge = 20
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ball, = plt.plot([], [], color = 'b')
ball2, = plt.plot([], [], 'o', color = 'b', ms  = 5)
ball3, = plt.plot([], [], color = 'r')
ball4, = plt.plot([], [], 'o', color = 'black')

def animate(i):
  ball.set_data(astroid(R = 1, t = np.linspace(0, 4*np.pi*i/frames, i)))
  ball2.set_data(astroid(R = 1, t = 4 * np.pi*i/frames))
  
  ball3.set_data(circle_func(R = 1, N = 200))
  ball4.set_data(astroid_func(R = 0.5, N = 200, t = i/frames))

ani = FuncAnimation(fig,
                   animate,
                   frames = frames,
                   interval = 20
                   )

plt.xlim(-2,2)
plt.ylim(-2,2)

ani.save('astroid.gif')



 #t = 4 * np.pi*i/frames
  # t = i/frames

#def animate(i):
  #ball.set_data(astroid(R = 1, t = np.linspace(0, 4*np.pi*i/frames, i)))
  #ball2.set_data(astroid(R = 1, t = i/frames))
  
  #ball3.set_data(circle_func(R = 1, N = 200))
  #ball4.set_data(astroid_func(R = 1, N = 200, t = np.linspace(0, 4*np.pi*i/frames)))