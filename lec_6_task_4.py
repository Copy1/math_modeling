import matplotlib.pyplot as plt         #логарифмическая спираль
import numpy as np
def log(A=1, k=4):
 fi = np.arange(-6*np.pi, 6*np.pi, 0.01)
 r = np.e**(A*fi)
 x = r*np.cos(fi)
 y = r*np.sin(fi)
 plt.plot(x, y)
 plt.show()
log()


def jesl(A=1, k=7):                                #спираль «жезл»
 fi = np.arange(-3*np.pi, 3*np.pi, 0.01)
 r = np.sin(k*(fi))
 x = r*np.cos(fi)
 y = r*np.sin(fi)
 plt.plot(x, y)
 plt.show()
jesl()


import matplotlib.pyplot as plt         #роза
import numpy as np
def rose(A=1, k=5):
 fi = np.arange(-4*np.pi, 4*np.pi, 0.01)
 r = np.e**(A*fi)
 x = r*np.cos(fi)
 y = r*np.sin(fi)
 plt.plot(x, y)
 plt.show()
rose()

