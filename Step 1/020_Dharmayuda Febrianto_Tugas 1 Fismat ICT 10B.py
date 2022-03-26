"""
TUGAS ICT FISMAT 1 BAGIAN B NO. 10
NAMA : Dharmayuda Febrianto
Kelas : FRE21
NIM : 21030224020
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as smp
from numpy import *
from matplotlib import *
from sympy import *
from mpmath import *
plt.style.use('classic')

x = np.linspace(-np.pi, np.pi, 200)
y = np.zeros(len(x))
labels = ['S1', 'S2', 'S3', 'S4']
plt.figure()
for n, label in zip(range(4), labels):
    y += (np.tan(x)**2)
    plt.plot(x, y, label=label)
plt.plot(x, np.cos(x), 'k', label='Analytic')
plt.grid()
plt.title('Grafik deret maclaurin')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right', prop={'size': 10})
plt.show()