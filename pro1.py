import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

#x0 = input('введите x: ')
#y0 = input('введите y: ')
fig, ax = plt.subplots()
x0 = 6
y0 = 8

#K = float(input('Модуль всестороннего сжатия(Н/м^2): '))
#p = float(input('Плотность жидкости(кг/м^3): '))
K = 5
p = 3
N = 20

c = np.sqrt(K/p)

balls = []

for i in range(N):
  ball, = plt.plot([], [], 'o', color='black', label='ball')
  balls.append(ball)

plt.plot(x0, y0, color='r', marker='o')

def circle_func(R, r):
  alpha = np.arange(0, 2*np.pi, 0.01)
  x = x0 + (R+r) * np.cos(alpha)
  y = y0 + (R+r) * np.sin(alpha)
  return x, y

edge = max(x0, y0)
plt.axis('equal')
ax.set_xlim(-2*edge, 2*edge)
ax.set_ylim(-2*edge, 2*edge)


def animate(i):
  for j in range(N):
    ball = balls[j]
    ball.set_data(circle_func(0, j+i))
  # ball2.set_data(circle_func(i, i))
  # ball3.set_data(circle_func(i, i+0.5))
  # ball4.set_data(circle_func(i, i+1.5))
  # ball5.set_data(circle_func(i, i+2))


ani = FuncAnimation(fig,
                    animate,
                    frames=np.arange(0, 5, 0.01),
                    interval = c
                    )



ani.save('pro1_animation.gif')


