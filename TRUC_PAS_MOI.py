#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:11:34 2025

@author: francoisdeberdt
"""

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
axe = fig.add_subplot(111, projection='3d')

dataForX = np.linspace(-10, 10, 100)
dataForY = np.linspace(-10, 10, 100)

dataForX, dataForY = np.meshgrid(dataForX, dataForY)

Z = np.sin(np.sqrt(dataForX**2 + dataForY**2))

surface = axe.plot_surface(dataForX, dataForY, Z, cmap='inferno', linewidth=0, antialiased=False)

fig.colorbar(surface, shrink=0.7, aspect=10)

axe.set_xlabel('X')
axe.set_ylabel('Y')
axe.set_zlabel('Z')

axe.set_title('3D Surface Plot')

plt.show()