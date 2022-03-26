#Defining Function
def f(x):
    return ((1/2*x)**3)-x-9

#Defining derivative of function
def g(x):
    return ((1/2*x)**3)-x-9

#Implementing Newton Raphson Method
def newtonRaphson (x0,e):
    step = 1
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION *** ')
    condition = True
    while condition:
        if g(x0)== 0.0:
            print('Devide by zero error!')
            break
        xl = x0 - f(x0)/g(x0)
        print('Iteration-%d,xl = %0.6 and f(xl)=%0.6' % (step, xl,f(xl)))
        x0=xl
        step = step + 1
        condition = abs (f(xl)) > e

        print('\nRequired root is: %0.8f' %xl)

#Input Section
x0 = input('Enter Guess: ')
e = input('Tolerable Error: ')

#Converting x0 and e to float
x0 = float(x0)
e = float(e)

#Starting Newton Raphson Method
newtonRaphson(x0,e)