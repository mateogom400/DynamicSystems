import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['lines.linewidth'] = 3
matplotlib.rcParams['font.size'] = 13
matplotlib.rcParams['lines.markersize'] = 5
matplotlib.rcParams['figure.figsize'] = (14, 9)
matplotlib.rc('text', usetex=True)
matplotlib.rc('axes', grid = False, labelsize=14, titlesize=16, ymargin=0.05)
matplotlib.rc('legend', numpoints=1, fontsize=11)

A1 = 2
A2 = 3
rho = 1000
k1 = 3e-5
k2 = 5e-5
pa = 1.013e5
g = 9.807
a2 = -7.5e-9
a1 = 5e-7
a0 = 1e-3

from scipy.optimize import fsolve
func1 = lambda p1 : (rho*g/A1)*(a2*(p1-pa)**2 + a1*(p1-pa) + a0 - k1*np.sqrt(p1-p2))
func2 = lambda p2 : (rho*g/A2)*(k1*np.sqrt(p1-p2) - k2*np.sqrt(p2-pa))

p1 = np.linspace(pa,pa+500,201)
p2 = np.linspace(pa,pa+500,201)
plt.plot(p1,func1(p1),label='p1')
plt.plot(p2,func2(p2),label='p2')
plt.xlabel(r"$p_1$",fontsize=20)
plt.ylabel(r"func",fontsize=20)
plt.legend(loc='upper right',fontsize=20)
plt.grid()
plt.show()

def hydrsys3_eq(p):
    p1 = p[0]
    p2 = p[1]
    A1 = 2
    A2 = 3
    rho = 1000
    k1 = 3e-5
    k2 = 5e-5
    pa = 1.013e5
    g = 9.807
    a2 = -7.5e-9
    a1 = 5e-7
    a0 = 1e-3
    pa = 1.013e5
    pdot = np.zeros(2)
    pdot[0] = (rho*g/A1)*(a2*(p1-pa)**2 + a1*(p1-pa) + a0 - k1*np.sqrt(p1-p2))
    pdot[1] = (rho*g/A2)*(k1*np.sqrt(p1-p2) - k2*np.sqrt(p2-pa))
    return pdot

pbar = fsolve(hydrsys3_eq, [101700, 101300])
print(pbar)

tf = 1000
N = 10000
h = tf/N
t = np.linspace(0.0,tf,num=N)
p = np.zeros((N,2))
pa = 1.013e5
p[0,0] = pa
p[0,1] = pa
for i in range(0,N-1):
    k1 = hydrsys3_eq(p[i,:])
    k2 = hydrsys3_eq(p[i,:]+0.5*h*k1)
    p[i+1,:] = p[i,:] + h*k2

p1bar = pbar[0]*np.ones(N)
p2bar = pbar[1]*np.ones(N)
plt.plot(t,p1bar,'r--',label=r"$\bar{p}_1$")
plt.plot(t,p2bar,'r--',label=r"$\bar{p}_2$")
plt.plot(t,p[:,0],'b',label=r"$p_1$")
plt.plot(t,p[:,1],'g',label=r"$p_2$")
plt.title("Respuesta paso",fontsize=20)
plt.xlabel(r"Tiempo [s]",fontsize=20)
plt.ylabel(r"$p$",fontsize=20)
plt.legend(loc='center right',fontsize=20)
plt.show()