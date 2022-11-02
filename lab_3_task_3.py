import numpy as np 

x0 = 43
y0 = 72
vx0 = 13
vy0 = 45
N = 5

coords = np.zeros((N, 3))
t = np.linspace(0 , 5, N)
x = x0 + vx0 * t
y = y0 + vy0 * t - 10 * t**2 / 2

for i in range(N):
  coords[i, 0] = t[i]
  coords[i, 1] = x[i]
  coords[i, 2] = y[i]
  print(coords)
  

