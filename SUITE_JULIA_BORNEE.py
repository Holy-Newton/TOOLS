# Creation of fractal figures on python.

from matplotlib import pyplot as plt
import numpy as np

Z0 = 0
c = 0.32 + 0.043j
liste = [0]

def Z1(n): return n**2 + c

for i in range(700000):
    if i==0:
        Z=Z0
    Z = Z1(Z)
    liste.append(Z)
    
x =[p.real for p in liste]
y =[p.imag for p in liste]
plt.figure()
plt.scatter(x, y, color = "red", s=5)


plt.title("Preuve suite Julia complexe bornée c = 0,32 + j0,043")
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.grid(True, linestyle="--", linewidth=0.5)
plt.show()

