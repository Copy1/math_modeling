import numpy as np          #гипербола
import matplotlib.pyplot as plt

x = np.linspace(-20, 15, 60)
y = np.linspace(-20, 15, 60)
X, Y = np.meshgrid(x, y)
fxy = ((x-1)**2 -1 - (y+3)**2/4)
plt.contour(X, Y, fxy, levels=[1], colors='g')
plt.show()



=================
import matplotlib.pyplot as plt       #парабола
import numpy as np
def parabola_plotter(a=1, b=1, c=0, title='Parabola plotter'):

    x = np.arange(-10, 10, 0.01)
    y = a*x**2 + b*x + c
 
    plt.plot(x, y, label='парабола')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title(title)
    plt.legend()

