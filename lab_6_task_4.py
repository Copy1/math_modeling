import numpy as np        
import matplotlib.pyplot as plt

x=np.linspace(0, 10, 1000)
y=[]

for i in range(1000):
  y1 = x[i]//1
  y.append(y1)

plt.plot(x, y)
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.show()



#y = N, если x ∈ [N, N+1], где N — целое число

