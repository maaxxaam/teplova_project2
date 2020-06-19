plank = 4.1*10**(-15) #i>k, i>=2, k>=1
for i in range(1,11):
    for j in range(1,11):
        if (i != j):
            Ei = -13.5 / i**2
            Ej = -13.5 / j**2
            omega = (Ei-Ej)/plank
            print('Для перехода между уровнями '+str(i)+' и '+str(j)+' требуется частота '+str(omega))
            
