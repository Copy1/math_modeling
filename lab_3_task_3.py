import numpy as np 
x0 = 78
y0 = 11
vx0 = 29
vy0 = 100

N = 10

coords = np.zeros((N, 3))
t = np.linspace(0 , 5, N)
x = x0 + vx0 * t
y = y0 + vy0 * t - 9.8 * t**2 / 2

for i in range(N):
  coords[i, 0] = t[i]
  coords[i, 1] = x[i]
  coords[i, 2] = y[i]
  print(coords)
  
