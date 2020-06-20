from typing import List

from sympy import *
import matplotlib.pyplot as plt
from math import radians
import cmath
import math


def fact(num):
    if num <= 1:
        return 1
    else:
        return num * fact(num - 1)


def lagger(al, ga):
    """
Calculates Lagger's polinominal. Takes three arguments: alpha, gamma and zeta
    """
    alpha, gamma, zeta = symbols('alpha gamma zeta')
    expr = diff(exp(zeta) * diff(zeta ** gamma * exp(-zeta), zeta, ga), zeta, al)
    return simplify(expr.subs({'alpha': al, 'gamma': ga}))  #


def legandra(me, l):
    """
Calculates Legander's polinominal. Takes four arguments: m, cos(theta) and l
    """
    cosTh, m, le = symbols('cosTh m le')
    expr = (1 - cosTh ** 2) ** (Abs(m) / 2) * diff(
        1 / ((2 ** le) * factorial(le)) * diff((cosTh ** 2 - 1) ** le, cosTh, l), cosTh, abs(me))
    return simplify(expr.subs({'m': me, 'le': l}))


def En(n):
    return (-(me * (e ** 4) * (z ** 2)) / ((4 * pi * e0) ** 2 * (2 * n ** 2 * h ** 2))) / e


e0 = 8.854187817e-12
E0 = 27.07
plank = 4.1e-15  # i>k, i>=2, k>=1
z = 1
me = 9.1e-31
a = 0.529
h = 1.05e-34
e = 1.602176634e-19
E = 28
Y = [0 for i in range(361)]
dec = 0
l = 2
m = 2
n = 3
R = list()
eps = -En(n) / E0
beta = (2 * eps) ** (1 / 2)  # z/n
final = [i for i in range(360)]
me, cosTheta, le = symbols('me cosTheta l')
legander = legandra(m, l)
coeff = ((fact(l - abs(m)) * (2 * l + 1) / (fact(l + abs(m)) * 4 * math.pi)) ** (1 / 2))
lagg = lagger(2*l+1, n+l)
for angle in range(361):
    phi = radians(angle)
    theta = radians(angle)
    print(angle)
    if angle % 180 == 0:
        continue
    spher = complex(legander.evalf(subs={'cosTh': math.cos(theta), 'm': m, 'le': l})) * \
        coeff * cmath.exp(1j * m * phi)
    Y[angle] = (spher.imag ** 2 + spher.real ** 2)
Anl = (1 / fact(2 * l + 1)) * (fact(n + l) / (2 * n * fact(n - l - 1))) ** 0.5 * (2 * z / n) ** 1.5
for rc in range(1, 11):
    print(n, l, rc)
    rho = rc
    R.append(Anl * (rho ** l) * math.exp(-beta * rho) * float(lagg.evalf(subs={'alpha': 2*l+1, 'gamma': n+l, 'zeta': 2*rho*beta})))
    plt.polar([radians(i) for i in range(361)], [i * R[-1] for i in Y], label='Rho = ' + str(rho))
plt.legend(loc='best')
plt.show()
