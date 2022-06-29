 import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x0 = input('введите x: ')
y0 = input('введите y: ')
fig, ax = plt.subplots()

K = float(input('Модуль всестороннего сжатия(Н/м^2): '))
p = float(input('Плотность жидкости(кг/м^3): '))
c = np.sqrt(K/p)
interval = 100 * c
N = 50

if c <= 30:
  c * 30 
print(c)

balls = []
wave, = plt.plot([], [], '-', color='black', label='ball')
for i in range(N):
  ball, = plt.plot([], [], '-', color='black', label='ball')
  balls.append(ball)

plt.plot(x0, y0, color='r', marker='o')

def circle_func(R, r, x0, y0):
  alpha = np.arange(0, 2*np.pi, 0.01)
  x = x0 + (R+r) * np.cos(alpha)
  y = y0 + (R+r) * np.sin(alpha)
  return x, y

edge = max(x0, y0)
plt.axis('equal')
ax.set_xlim(-2*edge, 2*edge)
ax.set_ylim(-2*edge, 2*edge)

j = 0
r = 0
def animate(i):
  global r, j
  r += 1
  ball = balls[j]
  ball.set_data(circle_func(0, r, x0, y0))
  j += 1
  for k in np.arange(0, 1, 0.1):
    wave.set_data(circle_func(0, r + k, x0, y0))

ani = FuncAnimation(fig,
                    animate,
                    frames=np.linspace(0, 5, N-2),
                    interval = interval
                    )


ani.save('pro1_animation.gif')





#x0 = 8
#y0 = 1
#K = 22000000
#p = 9970
#N = 50
