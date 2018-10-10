# import math

# def func(x):
# 	return x + 2*math.cos(x)

# def func2(x):
# 	out = [x[0]*math.cos(x[1]) - 4]
# 	out.append(x[1]*x[0] - x[1] - 5)
# 	return out

# from scipy.optimize import fsolve
# x0 = fsolve(func, 0.3)
# print(x0)

# x02 = fsolve(func2, [1, 1])
# print(x02)

import numpy as np
from scipy.optimize import fsolve

def hydrsys3_eq(p):
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
	p1 = p[0]
	p2 = p[1]
	pdot = np.zeros(2)
	pdot[0] = (rho*g/A1)*(a2*(p1-pa)**2 + a1*(p1-pa) + a0 - k1*np.sqrt(p1-p2))
	pdot[1] = (rho*g/A2)*(k1*np.sqrt(p1-p2) - k2*np.sqrt(p2-pa))
	return pdot

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

p1 = np.linspace(pa,pa+500,201)
p2 = np.linspace(pa,pa+500,201)
pdotg = hydrsys3_eq([p1,p2])

plt.plot(p1,pdotg[:,0],label='p1')
plt.plot(p2,pdotg[:,1],label='p2')
plt.xlabel(r"$p_1$",fontsize=20)
plt.ylabel(r"func",fontsize=20)
plt.legend(loc='upper right',fontsize=20)
plt.grid()
plt.show()

Psoln = fsolve(func, [101700, 101300])
print(Psoln)
