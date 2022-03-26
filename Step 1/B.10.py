print('Tugas ICT Fisika Matematika 1')
print('Kelas : Fisika 2021 E')
print('Bab   : Deret Tak Hingga')

print('Nama  : Riana Oktafianti')
print('NIM   : 21030224040')

print('Penyelesaian Tugas ICT FISMAT Bagian B No.10')

import sympy as smp
import numpy as np
import matplotlib.pyplot as plt
from mpmath import*
from numpy import*
from sympy import*
from matplotlib import*
plt.style.use('classic')

#Plot Grafik Deret McLaurint
x = np.linspace(-np.pi, np.pi, 200)
y = np.zeros(len(x))
labels = ['S1', 'S2', 'S3', 'S4']
plt.figure()
for n, label in zip(range(4), labels):
    y += (np.tan(x)**2)
    plt.plot(x,y, label = label)
plt.plot (x, np.cos(x), 'k', label = 'Analytic')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Deret Maclaurin')
plt.legend(loc='upper right',prop={'size':10})
plt.show()