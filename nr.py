#             CODE OF NEWTON RALPHSON METHOD  

import math

#      defining a function to find the derivative 

def derivative(f , x , dx = 1e-6):

    df = f(x + dx) - f(x - dx)
    return df/(2*dx)


#      defining a fuction newton which takes the function f, the initial value x0 ,the level of tolerance 
#               which is by default 1e-10 and taking maximum iteration limit as 100

def newton(f,x0,tol=1e-10,maxit=100):

    x=x0  #set current solution as x0
    fx=f(x)

    for _ in range(maxit):
        
        if abs(fx) < tol:
            break

        fpx= derivative(f,x)
        if abs(fpx) < tol:
            break

        x = x - fx/fpx
        fx = f(x)

    return x
    



func = lambda x:math.cos(x)-x*math.exp(x)
x0 = 1.0
x = newton(func,x0,tol= 1e-1,maxit=4)
print("Solution : x = {} , f(x) = {}".format(x, func(x)))
