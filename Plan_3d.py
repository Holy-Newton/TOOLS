#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 18:01:40 2025

@author: francoisdeberdt
"""

import numpy as np
from matplotlib import pyplot as plt

fonction = input("rentrez la fonction f(x,y):")

fig = plt.figure()
axe = fig.add_subplot(projection="3d")

x = y = np.linspace(-5, 5, 500)

x, y = np.meshgrid(x, y)

Z = eval(fonction)

surface = axe.plot_surface(x, y, Z)

plt.show()

