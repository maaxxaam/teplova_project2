#trying to do some project calcs
from sympy import *
import matplotlib.pyplot as plt
from math import pi, cos, radians
from cmath import exp
def fact(a):
    if a <= 1 : return 1
    else: return a*fact(a-1)
def legandra(me, cosTheta, l):
    '''
Calculates Legander's polinominal. Takes four arguments: m, cos(theta) and l
    '''
    cosTh, m, le = symbols('cosTh m le')
    expr = (1 - cosTh**2)**(Abs(m)/2)*diff(1/((2**le)*factorial(le))*diff((cosTh**2 - 1)**le, cosTh, l), cosTh, abs(me))
    #print(expr)
    func = lambdify(['cosTh','m','le'],expr)
    cosTh, m, le = cosTheta, me, l
    return func(cosTh, m, le)
eps = 1
E0 = 27.07
E = 28
eps = -E/E0
plank = 4.1*10**(-15) #i>k, i>=2, k>=1
z = 1
a = 0.529 * 10**(-10)
e = 1.6*10**(-19)
Y = [0 for i in range(361)]
dec = 0
l = 3
m = 0
phi = 1
theta = 0.5
for angle in range(361):
    phi = radians(angle)
    theta = radians(angle)
    print(angle)
    if (angle%180==0):
        Y[angle]=Y[angle-1]
        continue
    spher = ((fact(l-abs(m))*(2*l+1)/(fact(l+abs(m))*4*pi))**(1/2)*legandra(m,cos(theta),l)*exp((1j)*m*phi))
    Y[angle] = (spher.imag**2+spher.real**2)
#fig, ax = plt.subplots(figsize=(6, 6))
#ax = fig.add_subplot( projection='polar')
plt.polar([radians(i) for i in range(361)],Y)
#ax.plot(X,Y)
#ax.set_title('ХЗ')
#ax.set_ylabel('R(rho)')
#ax.set_xlabel('r*10**(-13)')
#ax.set_yscale('symlog')
#fig.tight_layout()
plt.show()
