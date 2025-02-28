import numpy as np
from matplotlib import pyplot as plt


M = np.zeros((3, 3))
P = np.ones((6, 6))

print(M)
print(P)

M_id = np.eye(3)
print(M_id)


x = np.linspace(-2, 2, 500)
y = np.linspace(-2, 2, 500)
X, Y = np.meshgrid(x, y)

Z = X + Y**2
#plt.grid(True)

plt.pcolormesh(X, Y, Z)

plt.show()