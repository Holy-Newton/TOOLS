#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:10:37 2025

@author: francoisdeberdt
"""

# First self made program with 3d visualisation:
 
    
import numpy as np
from matplotlib import pyplot as plt



x = np.linspace(-2, 2, 300)
y = np.linspace(-2, 2, 300)
Z = x**2*y

plt.figure("Z = X x Y")
axes = plt.axes(projection = '3d')

axes.plot(x, y, Z)
plt.show()

