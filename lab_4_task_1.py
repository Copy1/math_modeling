#  from random import random
# N = 10
 
# def average(a):
#     s = 0
#     for i in range(N):
#         s += a[i]
#     return s/N
 
# arr = [0] * N
# for i in range(N):
#     arr[i] = int(random() * 100)

# b = average(arr)
# print(arr)
# print(b)

# L = [1, 7, 9, 90]
# arf_funk(L)

def zoi_funс(L):
  
  S = 0
  for i in range(len(L)):
    S = S + L[i]
  return S/len(L)


L = [1, 7, 9, 90]
print(zoi_funс(L))

 




 