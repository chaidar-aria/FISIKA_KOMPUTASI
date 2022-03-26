import scipy.optimize as opt
y = lambda x:(1/2*x**3)-x-9
x = opt.newton(y,2.5)
print(x)
