#Simpons Rule estimation for integrals 
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

#asks user for # of steps to compute
print()
steps=int(input("How many steps? "))
print("Calculating...")
print()


#------------------------------------------------------------------------
#finding error estimate of the trapezoid approx. using sympy & scipy library which allows for finding K/M by caculating the deriviative & finding the maximum value


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
# print(posk_max)
# print(negk_max)
# print(k_max)
#sets K4 = to the maximum value found to use with error formula
K4=k_max

#calculates error using formula for trapezoid error and K2 (which is the maximum of |f``(x)|) which was estimated above
E=(K4*(b-a)**5)/(180*(steps)**4)


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
    Area=Area+4*f(x)
    x=x+dx
    Area=Area+2*f(x)
    x=x+dx

#adds yn to area
Area=Area+f(b)
#computes final area by multipling by (dx/2)
Areaf=(dx/3)*Area


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