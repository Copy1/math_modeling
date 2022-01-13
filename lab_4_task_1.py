def arf_funk(a, b, c, d, e):
 a = (f'Введите значение: ')
 b = (f'Введите значение: ')
 c = (f'Введите значение: ')
 d = (f'Введите значение: ')
 e = ({a} + {b} + {c} + {d} \ 4 )


 from random import random
N = 10
 
def average(a):
    s = 0
    for i in range(N):
        s += a[i]
    return s/N
 
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 100)

b = average(arr)
print(arr)
print(b)

L = [1, 7, 9, 90]
arf_funk(L)