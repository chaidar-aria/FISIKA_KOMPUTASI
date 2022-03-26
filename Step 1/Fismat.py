Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import sympy
import sympy as sym
from sympy.abc import x,y,z
z = x*y
sym.Derivative(z,y)
Derivative(x*y, y)
sym.diff(z,y)
x
z = x**2+2*y
sym.diff(z,x)
2*x
sym.diff(z,x,2)
2
sym.diff(x,y,z)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    sym.diff(x,y,z)
  File "C:\Users\LENOVO\AppData\Local\Programs\Python\Python310\lib\site-packages\sympy\core\function.py", line 2491, in diff
    return f.diff(*symbols, **kwargs)
  File "C:\Users\LENOVO\AppData\Local\Programs\Python\Python310\lib\site-packages\sympy\core\expr.py", line 3526, in diff
    return _derivative_dispatch(self, *symbols, **assumptions)
  File "C:\Users\LENOVO\AppData\Local\Programs\Python\Python310\lib\site-packages\sympy\core\function.py", line 1919, in _derivative_dispatch
    return Derivative(expr, *variables, **kwargs)
  File "C:\Users\LENOVO\AppData\Local\Programs\Python\Python310\lib\site-packages\sympy\core\function.py", line 1346, in __new__
    raise ValueError(filldedent('''
ValueError: 
Can't calculate derivative wrt x**2 + 2*y.
sym.diff(z,x,y)
0
#Soal Baru dari ebook fismat

from sympy.abc import x,y,t
y=x+sym.exp(x)-t
sym.idiff(y,