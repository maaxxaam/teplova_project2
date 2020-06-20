# trying to do some project calcs
from sympy import *
import matplotlib.pyplot as plt
from math import pi
import math


def fact(num):
    if num <= 1:
        return 1
    else:
        return num * fact(num - 1)


e0 = 8.854187817e-12
E0 = 27.07
plank = 4.1e-15  # i>k, i>=2, k>=1
z = 1
me = 9.1e-31
a = 0.529
h = 1.05e-34
e = 1.602176634e-19
R = list()
X = [((i - 1) % 100 + 1) / 10 for i in range(1, 1001)]
dec = 0


def lagger(al, ga):
    """
Calculates Lagger's polinominal. Takes three arguments: alpha, gamma and zeta
    """
    alpha, gamma, zeta = symbols('alpha gamma zeta')
    expr = diff(exp(zeta) * diff(zeta ** gamma * exp(-zeta), zeta, ga), zeta, al)
    return simplify(expr.subs({'alpha': al, 'gamma': ga}))  #


def En(n):
    return (-(me * (e ** 4) * (z ** 2)) / ((4 * pi * e0) ** 2 * (2 * n ** 2 * h ** 2))) / e


for n in range(2, 3):
    eps = -En(n) / E0
    beta = (2 * eps) ** (1 / 2)  # z/n
    for l in range(1, 2):
        lagg = lagger(2 * l + 1, n + l)
        Anl = 1 / fact(2 * l + 1) * (fact(n + l) / (2 * n * fact(n - l - 1))) ** 0.5 * (2 * z / n) ** 1.5
        for rho in range(1, 101):
            print(n, l, rho)
            R.append(Anl * ((rho/10) ** l) * math.exp(-beta * rho/10) * float(
                lagg.evalf(subs={'alpha': 2 * l + 1, 'gamma': n + l, 'zeta': 2 * rho * beta/10})))
            print(R[-1])
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.plot(X[dec * 100:dec * 100 + 100], R[dec * 100:dec * 100 + 100])
        ax.set_title('Радиальная функция при n = ' + str(n) + ' и l = ' + str(l))
        ax.set_ylabel('R(rho)')
        ax.set_xlabel('r*10**(-13)')
        # ax.set_yscale('symlog')
        fig.tight_layout()
        # print(R)
        dec += 1
plt.show()
