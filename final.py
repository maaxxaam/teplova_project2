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
print('Enter n, l, m separated by spaces: ')
n, l, m = [int(x) for x in input().split()]
R = list()
D = list()
eps = -En(n) / E0
beta = (2 * eps) ** (1 / 2)  # z/n
final = [i for i in range(360)]
legander = legandra(m, l)
coeff = ((fact(l - abs(m)) * (2 * l + 1) / (fact(l + abs(m)) * 4 * math.pi)) ** (1 / 2))
lagg = lagger(2*l+1, n+l)
for angle in range(361):
    phi = radians(angle)
    theta = radians(angle)
    print(angle)
    if angle % 180 == 0:
        Y[angle % 360] = Y[angle-1]
        Y[angle] = Y[angle-1]
        continue
    spher = complex(legander.evalf(subs={'cosTh': math.cos(theta)})) * \
        coeff * cmath.exp(1j * m * phi)
    Y[angle] = (spher.imag ** 2 + spher.real ** 2)
Anl = (1 / fact(2 * l + 1)) * (fact(n + l) / (2 * n * fact(n - l - 1))) ** 0.5 * (2 * z / n) ** 1.5
for rc in range(0, 101):
    print(n, l, rc)
    rho = rc/10
    R.append(Anl * (rho ** l) * math.exp(-beta * rho) * float(lagg.evalf(subs={'alpha': 2*l+1, 'gamma': n+l, 'zeta': 2*rho*beta})))
    D.append(R[-1]**2 * 4 * math.pi * rho**2)
    if rc % 10 == 0:
        plt.polar([radians(i) for i in range(361)], [i * R[-1] for i in Y], label='Rho = ' + str(rho))
plt.legend(loc='best')
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot([i/10 for i in range(101)], R)
ax.set_title('Радиальная функция при n = '+str(n)+' и l = '+str(l))
ax.set_ylabel('R(rho)')
ax.set_xlabel('rho')
fig.tight_layout()
fig, ay = plt.subplots(figsize=(6, 6))
ay.plot([i/10 for i in range(101)], [i**2 for i in R])
ay.set_title('Квадрат радиальной функции при n = '+str(n)+' и l = '+str(l))
ay.set_ylabel('|R(rho)|^2')
ay.set_xlabel('rho')
fig.tight_layout()
fig, az = plt.subplots(figsize=(6, 6))
az.plot([i/10 for i in range(101)], D)
az.set_title('Вероятность обнаружения электрона при n = ' + str(n) + ' и l = ' + str(l))
az.set_ylabel('D(rho)')
az.set_xlabel('rho')
az.set_yscale('symlog')
fig.tight_layout()
fig, aa = plt.subplots(figsize=(6, 6))
plt.polar([radians(i) for i in range(361)], Y, label='hello')
plt.show()
