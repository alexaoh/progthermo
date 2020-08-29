# Fraunhofer diffraction equation. 
# Use this to make a slit diffraction pattern.

import numpy as np
import matplotlib.pyplot as plt

def sinc(x):
    return np.sin(x)/x if x != 0 else 1

d = 1e-9 # Width of slit. 
l = 400e-9 # Wave length of light. 
I0 = 1 # Original intensity

def fraunhofer(theta):
    return I0*sinc(d*np.pi*np.sin(theta)/l)**2

def fraunhofer2(x):
    return I0*sinc(np.pi*x)**2

x = np.linspace(-4, 4, 100)

plt.plot(x, [fraunhofer2(i) for i in x])
plt.xlabel(r'$d \cdot \sin(\theta) / \lambda$')
plt.ylabel("Normalized intensity.")
plt.show()

# This could show the pattern from a single split diffraction experiment. 
