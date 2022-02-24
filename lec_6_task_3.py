import matplotlib.pyplot as plt         #эллипс
import numpy as np

def elips_plotter(radius=5):

    x = np.arange(-2*radius, 3*radius, 0.02)
    y = np.arange(-2*radius, 5*radius, 0.02)
    X, Y = np.meshgrid(x, y)
    fxy = X**2/16 + Y**2/3
    plt.contour(X, Y, fxy, levels=[1])
    plt.axis('equal')
    plt.show()
    
elips_plotter()

import matplotlib.pyplot as plt         #эллипс
import numpy as np

def elips_plotter(radius=5):

    x = np.arange(-2*radius, 3*radius, 0.02)
    y = np.arange(-2*radius, 5*radius, 0.02)
    X, Y = np.meshgrid(x, y)
    fxy = X**2 + Y**2
    plt.contour(X, Y, fxy, levels=[radius**2.5])
    plt.show()
    
elips_plotter()

======================
