#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 10:07:43 2025

@author: francoisdeberdt
"""

import matplotlib.pyplot as plt
import numpy as np
import statistics
from scipy.integrate import solve_ivp


### INTRO A L'UTILISATION DU MODULE solve_ivp DE scipy.integrate
"""

def fun(t, y): return -y
yo = [3]
sol = solve_ivp(fun , [0,1], yo, rtol = 1e-8, t_eval=np.linspace(0,1,20))  #ICI " rtole " règle la précision de calcul.

print('sol.t=',sol.t)
print('sol.y=',sol.y)
print('sol exacte y(1) =',3/np.exp(1))

plt.scatter(sol.t, sol.y)
plt.plot(sol.t,3/np.exp(sol.t) )
plt.show()



u=0
def Amplitude(t, y):
    global u
    if y[0] > u:
        u=y[0]
        
def fun(t, y): return y[1], -y[0]    ### ICI BIEN OBSERVER: ON OBTIENT UN TUPLE A DEUX ELEMENTS
def null(t, y): return y[0]

yo = [3, 0]
sol = solve_ivp(fun, [0,10], yo, rtol = 1e-8, t_eval=np.linspace(0,10, 100), events=null)


for t, y in zip(sol.t, sol.y.T):
    Amplitude(t, y)

#plt.plot(sol.t, 3* np.cos(sol.t))
plt.plot(sol.t, sol.y[0], linestyle='-')
plt.scatter(sol.t_events, 3*[0], s=120, c='red')

print(sol.t_events)
print(np.pi/2, 3*np.pi/2, 5*np.pi/2)
print(u)

plt.show()


"""
"""

def fun(t, y): return [y[1], -6*y[0]-5*y[1]]
yo = [5, 6]

sol =solve_ivp(fun, [0,10], yo, t_eval=np.linspace(0,10,100))

plt.plot(sol.t, sol.y[0], linestyle='--')
plt.grid(True)
plt.legend()
plt.title('Graphique résolution equ. diff')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()

"""




### Lorentz attractor:
    


#MES VARIABLES A ET B DU PROBLEME:
    
a = 10
b = 2.667
r = 28
t =80

def fun(t,state): 
    x, y, z = state
    dxdt = a*(y- x)
    dydt = x*(r- z) - y
    dzdt = x*y - b*z
    return [dxdt, dydt, dzdt]


yo = [1,1,1]

sol = solve_ivp(fun, [0, t], yo, t_eval=np.linspace(0, t, t*10))

fig = plt.figure()
axe = plt.axes(projection = '3d')
axe.plot(sol.y[0], sol.y[1], sol.y[2], lw=0.5, c='r')

axe.set_title(f'Lorentz Attractor with: a={a} b={b} r={r} ')
axe.set_xlabel('X')
axe.set_ylabel('Y')
axe.set_zlabel('Z')
plt.ion()
plt.show()
































































