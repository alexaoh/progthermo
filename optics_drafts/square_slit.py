"""Bottom of page 1: http://www.phys.unm.edu/msbahae/Optics%20Lab/Fourier%20Optics.pdf """

import numpy as np
import matplotlib.pyplot as plt

sinc = lambda x: np.sin(x)/x

I0 = 1 # E.g
a = 1e-3 # Width on x-axis.
b = 1e-3 # Width on y-axis.
lamda = 650E-9 # Wavelength (m).
N = 400        # Number of mesh points. 
x = np.linspace(-1e-3, 1e-3, N) # E.g
y = np.linspace(-1e-3, 1e-3, N) # E.g
xv, yv = np.meshgrid(x, y)
u = 2*np.pi*xv/lamda # Used the wrong coordinates here perhaps? 
v = 2*np.pi*yv/lamda # Used the wrong coordinates here perhaps?
I = I0*sinc(2*np.pi*u*a/2)**2*sinc(2*np.pi*v*b/2)**2

#plt.plot(xv, I)
#plt.plot(yv, I)
plt.imshow(I, extent=[195, 205, 195, 205]) # Shows some sort of diffraction in both y and x.
plt.colorbar()
plt.show()
