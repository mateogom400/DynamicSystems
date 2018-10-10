import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['lines.linewidth'] = 3
matplotlib.rcParams['font.size'] = 13
matplotlib.rcParams['lines.markersize'] = 5
matplotlib.rcParams['figure.figsize'] = (14, 9)
matplotlib.rc('text', usetex=True)
matplotlib.rc('axes', grid = False, labelsize=10, titlesize=10, ymargin=0.05)
matplotlib.rc('legend', numpoints=1, fontsize=11)

def hydrsys_eq(t, p1):    
    A = 2
    rho = 1000
    k = 5e-5
    pa = 1.013e5
    g = 9.807
    wibar = 6e-3
    pdot = (rho*g)/A * (wibar - k*math.sqrt(p1 - pa))
    return pdot

A = 2
rho = 1000
k = 5e-5
pa = 1.013e5
g = 9.807
wibar = 6e-3

tf = 10000
N = 10000
h = tf/N
t = np.linspace(0,tf,N)
p1 = np.zeros(N)
p1[0] = pa
for i in range(0,N-1):
    k1 = hydrsys_eq(t[i],p1[i])
    k2 = hydrsys_eq(t[i]+0.5*h,p1[i]+0.5*h*k1)
    p1[i+1] = p1[i] + h*k2

p1bar = wibar**2/k**2 + pa
p1bar = p1bar*np.ones(N)
plt.plot(t,p1,'b',label=r"$p_1$")
plt.plot(t,p1bar,'r--',label=r"$\bar{p}_1$")
plt.title("Respuesta paso",fontsize=10)
plt.xlabel(r"Tiempo [s]",fontsize=10)
plt.ylabel(r"$p_1$",fontsize=10)
plt.legend(loc='center right',fontsize=10)
plt.show()