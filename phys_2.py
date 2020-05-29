#trying to do some project calcs
import math
def fact(a):
    if a <= 1 : return 1
    else: return a*fact(a-1)
n = 1
l = 0
eps = 1
E0 = 27.07
E = 28
eps = -E/E0
beta = (2*eps)**0.5
z = n*beta
e = 1.6*10**(-19)
Anl = 1/fact(2*l+1)*(fact(n+l)/(2*n*fact(n-l+1)))**0.5*(2*z/n)**1.5
print(Anl)
