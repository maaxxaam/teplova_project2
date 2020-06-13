#trying to do some project calcs
from sympy import *
import matplotlib.pyplot as plt

def fact(a):
    if a <= 1 : return 1
    else: return a*fact(a-1)
def legandra(me, ee, cosTheta, l):
    '''
Calculates Legander's polinominal. Takes four arguments: m, e, cos(theta) and l
    '''
    cosTh, m, le, ele = symbols('cosTh m le ele')
    expr = (1 - cosTh**2)**(Abs(m)/2)*diff(1/((2**le)*factorial(le))*diff((cosTh**2 - 1)**le, cosTh, l), cosTh, abs(me))
    print(expr)
    func = lambdify(['cosTh','m','le','ele'],expr)
    cosTh, m, le, ele = cosTheta, me, l, ee
    return func(cosTh, m, le, ele)
eps = 1
E0 = 27.07
E = 28
eps = -E/E0
plank = 4.1*10**(-15) #i>k, i>=2, k>=1
z = 1
a = 0.529 * 10**(-10)
e = 1.6*10**(-19)
R = list()
X = [(i-1)%10+1 for i in range(1,101)]
dec = 0
'''for n in range (1, 5): 
    for l in range(n):
        for rc in range(1,11):
            r = rc*10**(-13)
            print(n, l, rc)
            beta = z/n
            rho = r/a
            Anl = 1/fact(2*l+1)*(fact(n+l)/(2*n*fact(n-l+1)))**0.5*(2*z/n)**1.5
            R.append(Anl * rho**l * e**(-beta*rho) * lagger(2*l+1,n+l,2*rho*beta))
            print(R[-1])
        fig, ax = plt.subplots(figsize=(6, 6))
        #fig, ay = plt.subplots(figsize=(6, 6))
        #fig, az = plt.subplots(figsize=(6, 6))
        ax.plot(X[dec*10:dec*10+10], R[dec*10:dec*10+10])
        ax.set_title('Радиальная функция при n = '+str(n)+' и l = '+str(l))
        ax.set_ylabel('R(rho)')
        ax.set_xlabel('r*10**(-13)')
        ax.set_yscale('symlog')
        '''''''ay.plot(t, x)
        ay.set_title('Движение маятника Фуко')
        ay.set_ylabel('X')
        ay.set_xlabel('t')
        az.plot(t, y)
        az.set_title('Движение маятника Фуко')
        az.set_ylabel('Y')
        az.set_xlabel('t')''''''
        fig.tight_layout()
        print(R)
        dec += 1
plt.show()'''
print(legandra(1,1,0.5,1))
