#Definition Fungction
def f(x):
    return 4*x**3 +7*x + 3
#Definition derevative of function
def g(x):
    return 12*x**2 + 7
#Implemantation Newton Rapshon Method
def newtonRaphson (x0,e):
    step = 1
    print("\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION***")
    condition = True
    while condition:
        if g(x0)==0.0:
            print("Divide by zero error!")
            break
        x1 = x0 - f(x0)/g(x0)
        print ('iteration-%d, x1 = %0.6f and f(x1) =%0.6f'%(step, x1, f(x1)))
        x0=x1
        step = step + 1
        condition = abs(f(x1))> e

        print('\nRequired root is: %0.8f'% x1)

#Input Section
x0 = input('Enter Guess:')
e = input('Tolerable Error:')

#Converting x0 and e to float
x0 = float(x0)
e  = float(e)

#Starting Newton Raphson Method
newtonRaphson(x0,e)
