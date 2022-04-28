import random
import math
c = 100 + random.randint(0, 900)
print(c)
print(list(map(int,str(c))))
b = list(map(int,str(c)))+(list(map(int,str(c))))
print(b)
