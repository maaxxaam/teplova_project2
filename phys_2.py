#trying to do some project calcs
from sympy import *
def fact(a):
    if a <= 1 : return 1
    else: return a*fact(a-1)
for n in range (1, 5): 
    for l in range(n):
        for rc in range(1,11):
            r = rc*10**(-11)
            print(n, l, rc)
            eps = 1
            E0 = 27.07
            E = 28
            eps = -E/E0
            z = 1
            beta = z/n
            a = 0.529 * 10**(-10)
            rho = r/a
            e = 1.6*10**(-19)
            def lagger(al, ga, ze):
                '''
            Calculates Lagger's polinominal. Takes three arguments: alpha, gamma and zeta
                '''
                el = 1.6*10**(-19)
                alpha, gamma, zeta, ele = symbols('alpha gamma zeta ele')
                expr = diff(ele**zeta * diff(zeta**gamma * ele**(-zeta), zeta, ga), zeta, al)
                func = lambdify(['alpha','gamma','zeta','ele'],expr)
                alpha, gamma, zeta, ele = al, ga, ze, el
                return func(alpha, gamma, zeta, el)
                
            Anl = 1/fact(2*l+1)*(fact(n+l)/(2*n*fact(n-l+1)))**0.5*(2*z/n)**1.5
            Rnl = Anl * rho**l * e**(-beta*rho) * lagger(2*l+1,n+l,2*rho*beta)
            print(Rnl)
