"""https://www.spiedigitallibrary.org/conference-proceedings-of-spie/10452/1045218/Optics-simulations-a-Python-workshop/10.1117/12.2268377.full 

Make GUI/Widgets in Jupyter Notebook with ipywidgets, inspired by GUI made in article above. 
"""
import numpy as np
import matplotlib.pyplot as plt

# This does not look like Fraunhofer diffraction (far-fetched), since distance to screen is considered. 
# The distance to the screen decides how much the pattern spreads, which makes sense! This needs to be here! Correct!

lamda = 650E-9 # Wavelength (m).
b = 1.0E-3     # Slit-width (m).
a = 2.5E-3     # Distance between slits (m).
D = 2          # Screen distance (m).
e = 1E-2       # Size of screen (m).
N = 400        # Number of mesh points. 

# L_min \approx 1.5 for the config above. 

x_max = e/2 ; x_min = -e/2 # Coordinates of screen. 
x = np.linspace(x_max, x_min, N)
B = (np.pi*b*x)/(lamda*D) # Intermediate variable.
A = (np.pi*a*x)/(lamda*D) # Intermediate variable. 
I = 0.5*(np.sin(B)/B)**2 * (1+np.cos(2*A)) # The last factor is the same as 2*np.cos(A)**2
envelope = (np.sin(B)/B)**2

# Plotting: 
fig = plt.figure(figsize=(8,5))
#fig.suptitle("Young Double Slit", fontsize=14, fontweight="bold")
ax1 = fig.add_subplot(111)
ax1.grid(True)
ax1.plot(x, I, '-k', linewidth=3)
ax1.plot(x, envelope, '--k', linewidth=2, alpha=0.8)
ax1.set_xlim(x_min, x_max)
ax1.set_xlabel(r"$x \ (m)$", fontsize=14, fontweight="bold")
ax1.set_ylabel(r"$I(x,y)/I_0$", fontsize=14, fontweight="bold")
ax1.set_title((r"$wavelength \ \lambda = %.1e \ m, "
    "\ b = %.1e \ m, \ a = %.1e \ m, \ D = %.0e \ m$"% (lamda, b, a, D)))
plt.show()
 
# Can make something similar for single-slit! Page 326, Pedrotti. 
# The equations are a tad different here from in Pedrotti, but tehy seem to be very similiar. 
