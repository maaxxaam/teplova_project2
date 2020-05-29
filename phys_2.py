#trying to do some project calcs
import math
def fact(a):
    if a <= 1 : return 1
    else: return a*fact(a-1)
n = 1
l = 0
z = 1
eps = 1
Anl = 1/fact(2*l+1)*(fact(n+l)/(2*n*fact(n-l+1)))**1/2*(2*z/n)**3/2
print(Anl)
