#Элементы массива NxM вычисляются по формуле A[i, j] = sin(N · i + M · j) при индексации с единицы или по формуле A[i, j] = sin(N · (i+1) + M · (j + 1)) при индексации с нуля. Если полученный таким образом элемент массива отрицателен, то заменить его на 0. Вывести конечный массив на экран.
import numpy as np
import math as m

   

N = input('введите с клавиаьтуры  ')
M = input(" введите с клавиатуры  ")
A = np.zeros(N, M)

for i in range({N}):
  for j in range({M}):
    print(i, j)
    if i == 0 and j == 0:
      A[i, j] = m.sin({N} * i + {M} * j)
    else:
      A[i, j] = m.sin({N} * (i+1) + {M} * (j + 1))
  if i < 0:
        if j < 0:
          i == 0
          j == 0
        

print(A)


    