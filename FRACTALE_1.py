#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 20:17:55 2025

@author: francoisdeberdt
"""


#First try to try modelising a fractal:
    
    
import numpy as np
import matplotlib.pyplot as plt

N = 2000

C = 0.32+0.043j
M = np.zeros((N,N))

x = np.linspace(-2, 2, N)
y = np.linspace(-2, 2, N)
x, y = np. meshgrid(x, y)
z = x + 1j*y

def f(n):
    count = 0
    while abs(n)<2 and count<100:
        n = n**2 + C
        count +=1
    return count

for i in range(N):
    for j in range(N):
        M[i,j]=f(z[i,j])

plt.imshow(M, cmap='magma', origin='lower')
plt.colorbar()
plt.show()
    