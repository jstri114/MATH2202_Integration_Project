#Trapezoidal estimation for integrals 
# by Jonathan Strickland
# for MATH 2202.11


# library imports
import math 
import time
import sympy as sym
import scipy
from sympy import lambdify


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
E=int(input("What should the prescribed error be? "))
print("Calculating...")
print()


#------------------------------------------------------------------------
#finding number of steps to take based on prescribed error target of the trapezoid approx. using sympy & scipy library which allows for finding K/M by caculating the deriviative & finding the maximum value


#declare x as variable to be used for sym.py
x = sym.Symbol('x')
#takes the first derivative of the function using the function fs(x), which is the orginal function but using sympy syntax
fd1=sym.diff(fs(x))
#takes the second derivative
fd2=sym.diff(fd1)

#convert the sympy function fd2 from symbolic form to regular form to use with scipy
k=lambdify(x, fd2, 'numpy')

#cannot use optimize on |k(x)|, so must find +/-k(x) seperately then compare to find |k(x)|
#uses optimize.mimimize_scalar to find the minimum value of a function, bounded by the domain given earlier [a,b]
poskmin = scipy.optimize.minimize_scalar(lambda x: k(x), bounds=[a,b], method='bounded')
negkmin = scipy.optimize.minimize_scalar(lambda x: -k(x), bounds=[a,b], method='bounded')
#stores the absolute values of each result so they can be compared with max function
posk_max=abs(k(poskmin.x))
negk_max=abs(k(negkmin.x))
#finds greater value between the two to obtain |k(x)|
k_max=max(posk_max,negk_max)
# print(posk_max)
# print(negk_max)
# print(k_max)
#sets K2 = to the maximum value found to use with error formula
K2=k_max

#calculates steps using formula for trapezoid error and K2 (which is the maximum of |f``(x)|) which was estimated above, but given E from input to find # of steps
steps=((K2*(b-a)**3)/(12*E))**(1/2)

#------------------------------------------------------------------------
#start of estimation
tstart=time.time()
#------------------------------------------------------------------------
#finding the estimated integral for f(x) using trapezoid approx.


#calculates the width (dx) of each step
dx=(b-a)/steps
#add f(0) to Area by setting set x = a (lower bound)
x=a
Area=f(x)
#makes x = x1 by adding dx to prepare for recursive loop
x=x+dx

#computes yx and adds it to total area, starting with x1 and adding dx each time to ensure the next loop runs with x2, x3, xn-1 and so on
while x < b:
    Area=Area+2*f(x)
    x=x+dx

#adds yn to area
Area=Area+f(b)
#computes final area by multipling by (dx/2)
Areaf=(dx/2)*Area


#------------------------------------------------------------------------
#end of estimation
tend = time.time()
telapsed = tend - tstart
#------------------------------------------------------------------------
#outputing results
print("The estimated integral is "+str(Areaf)+" using "+str(steps)+" steps.")
print("The time elasped for integral estimation was "+str(telapsed)+" seconds.")
print("The error is "+str(E)+".")
print()