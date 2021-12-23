import numpy as np 

N = 5
M = 3

A = np.zeros((N, M))

for i in range(N):
  for j in range(M):
    print(i, j)
    if i == 0 and j == 0:
        A[i, j] = np.sin(N * i + M * j)
    else:
      A[i, j] = np.sin(N * (i + 1) + M * (j + 1))
    
for i in range(N):
  for j in range(M):
    if  A[i, j] < 0:
       A[i, j] = 0
 
print(A)

