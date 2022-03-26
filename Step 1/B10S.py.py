from mpmath import*

#Perhitungan Pendekatan Limit
print('pendekatan limit')
y = lambda x:(tan**2)*x
print(limit(y,inf))

#Koeffisien Deret McLaurint
print ('koeffisien Deret Maclaurint')
f=lambda x: (tan**2)*x
nprint([diff(f, 0, n) for n in range(5)])

#Plot Grafik Deret McLaurint
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-np.pi, np.pi, 200)
y = np.zeros(len(x))
labels = ['S1', 'S2', 'S3', 'S4']
plt.figure()
for n, label in zip(range(4), labels):
    y = y + (x**2*n/ np.math.factorial(2*n))
    plt.plot(x,y, label = label)
plt.plot(x, (np.tan**2)*2, 'k', label = 'Analytic')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right',prop={'size':10})
plt.show()
