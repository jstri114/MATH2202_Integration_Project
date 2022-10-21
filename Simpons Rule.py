#Simpson's Rule estimation for integrals 
# by Jonathan Strickland
# for MATH 2202.11


# library imports
import math 
import time
import sympy as sym
from sympy import lambdify
import scipy
import sys


#defines f(x), the function to integrate
def f(x):
    return x*math.sin(x**2)
#defines f(x), the function to integrate, but in symbolic form which sympy can use
def fs(x):
    return x*sym.sin(x**2)
#defines the limits for the function
(a,b)=(0,1)

#asks user for # of steps to compute
print()
steps=int(input("How many steps? "))
if (steps % 2) != 0:
    sys.exit("Error: odd number of steps, please adjust to a even number of steps")
print("Calculating...")
print()


#------------------------------------------------------------------------
#finding error estimate of the trapezoid approx. using sympy & scipy library which allows for finding K/M by calculating the derivative & finding the maximum value


#declare x as variable to be used for sym.py
x = sym.Symbol('x')
#takes the 1st derivative of the function using the function fs(x), which is the original function but using sympy syntax
fd1=sym.diff(fs(x))
#takes the 2nd derivative
fd2=sym.diff(fd1)
#takes the 3rd derivative
fd3=sym.diff(fd2)
#takes the 4th derivative
fd4=sym.diff(fd3)

#convert the sympy function fd4 from symbolic form to regular form to use with scipy
k=lambdify(x, fd4, 'numpy')

#cannot use optimize on |k(x)|, so must find +/-k(x) separately then compare to find |k(x)|
#uses optimize.minimize_scalar to find the minimum value of a function, bounded by the domain given earlier [a,b]
#bounded method uses Brent's algorithm to find a minimum value on the function within the bounds
poskmin = scipy.optimize.minimize_scalar(lambda x: k(x), bounds=[a,b], method='bounded')
negkmin = scipy.optimize.minimize_scalar(lambda x: -k(x), bounds=[a,b], method='bounded')
#stores the absolute values of each result so they can be compared with max function
posk_max=abs(k(poskmin.x))
negk_max=abs(k(negkmin.x))
#finds greater value between the two to obtain |k(x)|
k_max=max(posk_max,negk_max)
#sets K4 = to the maximum value found to use with error formula
K4=k_max

#calculates error using formula for trapezoid error and K2 (which is the maximum of |f``(x)|) which was estimated above
E=(K4*(b-a)**5)/(180*(steps)**4)


#------------------------------------------------------------------------
#start of estimation
tstart = time.perf_counter()
#------------------------------------------------------------------------
#finding the estimated integral for f(x) using trapezoid approx.


#calculates the width (dx) of each step
dx=(b-a)/steps
#adds y0 to Area by setting set x = a (lower bound)
x=a
Area=f(x)
#sets loop counter = 0, this keeps track of how many intervals have been computed as using x would result in extra loops due to rounding errors
loopsteps=0
#computes yx and adds it to total area, starting with x1 and adding dx each time to ensure the next loop runs with x2, x3, xn-1 and so on
while loopsteps < steps-1:
    x=x+dx
    Area=Area+4*f(x)
    loopsteps=loopsteps+1
    if loopsteps < steps-1:
        x=x+dx
        Area=Area+2*f(x)
    loopsteps=loopsteps+1
#adds yn to area
Area=Area+f(b)
#computes final area by multiplying by (dx/3)
Areaf=(dx/3)*Area


#------------------------------------------------------------------------
#end of estimation
tend = time.perf_counter()
telapsed = tend - tstart
#------------------------------------------------------------------------
#outputting results
print("The estimated integral is "+str(Areaf)+" using "+str(steps)+" steps.")
print("The time elapsed for integral estimation was "+str(telapsed)+" seconds.")
print("The error is "+str(E)+".")
print()