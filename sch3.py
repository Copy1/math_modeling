import random
import math
num = 100 + random.randint(0, 900)
print('num:', num)
print()
s = 0
for i in f'{num}':
  print(i)
  s += int(i)

print()
print('s:', s)
