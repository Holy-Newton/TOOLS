import numpy as np
import matplotlib.pyplot as plt

x1, y1 = np.loadtxt("data_2.txt", unpack=True, comments="#")
x0, y0 = np.loadtxt("data_1.txt", unpack=True, comments="#")


def coef_1(x,y):
    total,a, size = 0,0,len(x)
    for i in range(size):
        if x[i] == 0: a=y[i]
        else: total += (y[i]-a)/x[i] 
    return total/size, a

def variance(x,y):
    total,V, size = 0,0,len(x)
    for i in range(size):
        total += y[i]/x[i]
    for i in range(size-1):
        V += ((y[i+1]/x[i+1]-total/size)**2)/size
    return V

def output_control(ax_n, x, y, name):
    ax_n.scatter(x,y, color = "black", marker="+")
    
    x_lin = np.linspace(0, max(x))
    ax_n.plot(x_lin, coef_1(x,y)[1] + x_lin * coef_1(x,y)[0], color = "red")
    ax_n.text(max(x)*0.6, max(y)*0.9, f" {round(coef_1(x,y)[0], 3)} x + {round(coef_1(x,y)[1], 3)} ", fontsize=14)
    ax_n.set_title(name)


fig, axs = plt.subplots(2, sharex=False, sharey=False)
output_control(axs[0] ,x0, y0, "data_1 linear regression")
output_control(axs[1] ,x1, y1, "data_2 linear regression")
print(variance(x0,y0))
print(variance(x1,y1))


plt.show()