from sympy import *
import matplotlib.pyplot as plt

def fact(a):
    if a <= 1 : return 1
    else: return a*fact(a-1)
def lagger(al, ga, ze):
    '''
Calculates Lagger's polinominal. Takes three arguments: alpha, gamma and zeta
    '''
    alpha, gamma, zeta = symbols('alpha gamma zeta')
    expr = diff(exp(zeta) * diff(zeta**gamma * exp(-zeta), zeta, ga), zeta, al)
    func = lambdify(['alpha','gamma','zeta'],expr)
    alpha, gamma, zeta = al, ga, ze
    return func(alpha, gamma, zeta)
def legandra(me, ee, cosTheta, l):
    '''
Calculates Legander's polinominal. Takes four arguments: m, e, cos(theta) and l
    '''
    cosTh, m, le, ele = symbols('cosTh m le ele')
    expr = (1 - cosTh**2)**(Abs(m)/2)*diff(1/((2**le)*factorial(le))*diff((cosTh**2 - 1)**le, cosTh, l), cosTh, abs(me))
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
Y = [0 for i in range(361)]
dec = 0
l = 3
m = 2
R = list()
final = list()
for angle in range(361):
    phi = radians(angle)
    theta = radians(angle)
    print(angle)
    if (angle%180==0):continue
    spher = ((fact(l-abs(m))*(2*l+1)/(fact(l+abs(m))*4*pi))**(1/2)*legandra(m,e,cos(theta),l)*exp((1j)*m*phi))
    Y[angle] = (spher.imag**2+spher.real**2)
        for rc in range(1,11):
            r = rc*10**(-13)
            print(n, l, rc)
            beta = z/n
            rho = r/a
            Anl = 1/fact(2*l+1)*(fact(n+l)/(2*n*fact(n-l+1)))**0.5*(2*z/n)**1.5
            R.append(Anl * rho**l * e**(-beta*rho) * lagger(2*l+1,n+l,2*rho*beta))
            print(R[-1])
fig, ax = plt.subplots(figsize=(6, 6))
ax = fig.add_subplot( projection='polar')
ax.plot([radians(i) for i in range(361)],Y)
#ax.plot(X,Y)
ax.set_title('ХЗ')
ax.set_ylabel('R(rho)')
ax.set_xlabel('r*10**(-13)')
#ax.set_yscale('symlog')
fig.tight_layout()
plt.show()
print(spher)

