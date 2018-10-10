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

A = 2
rho = 1000
k = 5e-5
pa = 1.013e5
g = 9.807
wibar = 6e-3

from scipy.optimize import fsolve
a2 = -7.5e-9
a1 = 5e-7
a0 = 1e-3
func = lambda p1 : (rho*g/A)*(a2*(p1-pa)**2 + a1*(p1-pa) + a0 - k*np.sqrt(p1-pa))

p1 = np.linspace(pa,pa+400,201)
plt.plot(p1,func(p1))
plt.xlabel(r"$p_1$",fontsize=20)
plt.ylabel(r"func",fontsize=20)
plt.grid()
plt.show()

p1_initial = 101500
p1_soln = fsolve(func, p1_initial)
deltapbar = p1_soln-pa
wi_bar = a2*(p1_soln-pa)**2 + a1*(p1_soln-pa) + a0
print(deltapbar)
print(wi_bar)

deltap = np.linspace(0.0,500,100)
w_v = k*np.sqrt(deltap)
plt.plot(w_v,deltap,label='Valvula')
w_p = -7.5e-9*deltap**2 + 5e-7*deltap + 1e-3
plt.plot(w_p,deltap,label='Bomba')
plt.plot(wi_bar,deltapbar, marker='o', markersize=10, color='red')
plt.xlabel(r"$w$",fontsize=20)
plt.ylabel("$\Delta p$",fontsize=20)
plt.legend(loc='upper left',fontsize=20)
plt.xlim(0,0.001)
plt.ylim(0,500)
plt.show()

def hydrsys2_eq(t, p1):    
    A = 2
    rho = 1000
    k = 5e-5
    pa = 1.013e5
    g = 9.807
    a2 = -7.5e-9
    a1 = 5e-7
    a0 = 1e-3
    pdot = (rho*g/A)*(a2*(p1-pa)**2 + a1*(p1-pa) + a0 - k*math.sqrt(p1-pa))
    return pdot

tf = 1000
N = 10000
h = tf/N
t = np.linspace(0.0,tf,num=N)
p1 = np.zeros(N)
p1[0] = pa
for i in range(0,N-1):
    k1 = hydrsys2_eq(t[i],p1[i])
    k2 = hydrsys2_eq(t[i]+0.5*h,p1[i]+0.5*h*k1)
    p1[i+1] = p1[i] + h*k2

p1bar = p1_soln*np.ones(N)
plt.plot(t,p1,'b',label=r"$p_1$")
plt.plot(t,p1bar,'r--',label=r"$\bar{p}_1$")
plt.title("Respuesta paso",fontsize=20)
plt.xlabel(r"Tiempo [s]",fontsize=20)
plt.ylabel(r"$p_1$",fontsize=20)
plt.legend(loc='center right',fontsize=20)
plt.show()