import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
	
fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='green', label='ball')

def circle_move(R):
  alpha = np.arange(0, 2*np.pi, 0.01)
  x = R * np.cos(alpha)
  y = R * np.sin(alpha)
  return x, y

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
  ball.set_data(circle_move(R=i))
 
ani = FuncAnimation(fig,
                    animate,
                    frames=np.arange(0, 5, 0.01),
                    interval=30
                    )
de













#plt.show()
ani.save('lab_7_task_2_animation.gif')


