def fact(a):
    if a <= 1 : return 1
    else: return a*fact(a-1)
eps = 1
E0 = 27.07
E = 28
eps = -E/E0
plank = 4.1*10**(-15) #i>k, i>=2, k>=1
z = 1
a = 0.529 * 10**(-10)
e = 1.6*10**(-19)
for i in range(1,11):
    for j in range(1,11):
        if (i != j):
            Ei = -13.5 / i**2
            Ej = -13.5 / j**2
            omega = (Ei-Ej)/plank
            print('Для перехода между уровнями '+str(i)+' и '+str(j)+' требуется частота '+str(omega))
            
