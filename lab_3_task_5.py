import numpy as np 

N = 6
M = 19

A = np.zero(N, M)

for i in range(N):
  for j in range(M):
    if i == 0 and j == 0:
      A[i, j] = np.sin(N * i + M * j)
    else:
      A[i, j] = np.sin(N * (i + 1) + M * (j + 1))

print(A) \n ptint()

B = A[::, 1]
C = A[::, 2]

A[::, 1] = C
A[::, 2] = B
print(A)
