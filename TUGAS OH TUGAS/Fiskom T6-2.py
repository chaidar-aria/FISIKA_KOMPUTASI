import scipy.optimize as opt
y = lambda x:4*(x**3)+7*x+3
x = opt.bisect(y,-0.5,-0.4,xtol=0.00005)
print(x)
