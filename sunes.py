# %%
from matplotlib import *
from numpy import *
import matplotlib.pyplot as plt
import numpy as np

# %%
# Definisi fungsi f(x) dengan


def f(x):
    return -3*x**3-5*x-9


# %%
tol = 0.005  # Toleransi
delta = 1000
a = -1
b = -1.5
fa = f(a)
fb = f(b)
xd = []
xn = b

while delta > tol:
    # Nilai tengah
    c = (a+b)/2.0
    fc = f(c)

    # Cek jika interval mengandung solusi
    if(fa*fc) < 0:
        b = c
        fb = fc
    else:
        a = c
        fa = fc

    xd.append(c)
    xnp1 = c
    delta = abs(xnp1-xn)

    # Simpan untuk iterasi berikutnya
    xn = xnp1
print(xd)


# %%
# Visualisasi
n = np.arange(len(xd))
plt.plot(n, xd, '-or')
plt.xlabel('$n$')
plt.ylabel('$x_n$')
plt.show()


# %%
