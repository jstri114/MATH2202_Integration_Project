#Simpons Rule estimation with specific error for integrals 
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
#defines the limts for the function
(a,b)=(0,1)

#asks user for prescribed error to compute
print()
pE=float(input("What should the prescribed error be? "))
print("Calculating...")
print()


#------------------------------------------------------------------------
#finding number of steps to take based on prescribed error target of the simpons rule approx. using sympy & scipy library which allows for finding K/M by caculating the deriviative & finding the maximum value


#declare x as variable to be used for sym.py
x = sym.Symbol('x')
#takes the 1st derivative of the function using the function fs(x), which is the orginal function but using sympy syntax
fd1=sym.diff(fs(x))
#takes the 2nd derivative
fd2=sym.diff(fd1)
#takes the 3rd derivative
fd3=sym.diff(fd2)
#takes the 4th derivative
fd4=sym.diff(fd3)

#convert the sympy function fd4 from symbolic form to regular form to use with scipy
k=lambdify(x, fd4, 'numpy')

#cannot use optimize on |k(x)|, so must find +/-k(x) seperately then compare to find |k(x)|
#uses optimize.mimimize_scalar to find the minimum value of a function, bounded by the domain given earlier [a,b]
poskmin = scipy.optimize.minimize_scalar(lambda x: k(x), bounds=[a,b], method='bounded')
negkmin = scipy.optimize.minimize_scalar(lambda x: -k(x), bounds=[a,b], method='bounded')
#stores the absolute values of each result so they can be compared with max function
posk_max=abs(k(poskmin.x))
negk_max=abs(k(negkmin.x))
#finds greater value between the two to obtain |k(x)|
k_max=max(posk_max,negk_max)
#sets K4 = to the maximum value found to use with error formula
K4=k_max

#calculates steps using formula for trapezoid error and K2 (which is the maximum of |f``(x)|) which was estimated above, but given E from input to find # of steps
rawsteps=((K4*(b-a)**5)/(180*pE))**(1/4)
#rounds steps up to nearest even whole number
steps=2*math.ceil(rawsteps/2)
#caculate the actual error after rounding the steps
E=(K4*(b-a)**5)/(180*(steps)**4)
#convert actual error to float for proper displaying
float(E)


#------------------------------------------------------------------------
#start of estimation
tstart = time.perf_counter()
#------------------------------------------------------------------------
#finding the estimated integral for f(x) using trapezoid approx.


##calculates the width (dx) of each step
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
#computes final area by multipling by (dx/3)
Areaf=(dx/3)*Area


#------------------------------------------------------------------------
#end of estimation
tend = time.perf_counter()
telapsed = tend - tstart
#------------------------------------------------------------------------
#outputing results
print("The estimated integral is "+str(Areaf)+" using "+str(steps)+" steps.")
print("The time elasped for integral estimation was "+str(telapsed)+" seconds.")
print("The target error was "+str(pE)+", the actual error was "+str(E)+".")
print()