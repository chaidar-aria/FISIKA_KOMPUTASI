# FISIKA KOMPUTASI | SISTEM PERSAMAAN LINEAR

# Kelompok 5
# No 5 | Metode Gauss Seidel

import numpy as np
import sympy as smp


#Initial setup
x0 = 0
y0 = 0
z0 = 0
count = 1
# Reading tolerable erroe
e = float(input('Enter tolerable  error: '))

# Implementation of Gauss Seidel Iteration
print('\nCount\tx\ty\tz\n')

condition = True

while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x1,y0,z0)
    z1 = f3(x1,y1,z0)
    print('%d\t%0.4f\t%0.4f\n' &(count, x1,y1,z1))
    e1 = abs(x0-x1);
    e2 = abs(y0-y1);
    e3 = abs(z0-z1);

    
