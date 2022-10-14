#example test code with print and input commands
import math 
import time
import sympy as sym

#print("Hello World")
#print("This is the year "+str(2022)+".")
#name = input("What is your name?")
#print("Welcome "+str(name)+"!")

#n = int(input("The factorial of "))
#factorial = 1;
#for i in range(n):
#    factorial = factorial*(i+1)
#print("is "+str(factorial)+".")

#n= int(input("The factorial of "))
#iteration = 0
#factorial =1
#while iteration < n:
#    iteration = iteration + 1
#    factorial = factorial*iteration
#print("is "+str(factorial)+".")

# while 1:
#     n = int(input("What n? "))
#     a0 = int(input("starting value for a0? "))
#     an = a0
#     counter = 1
#     while counter < n+1:
#       an = sqrt(2+sqrt(an))
#       print (an)
#       counter = counter+1
#     print("The final number is "+str(an)+"!")

#defines f(x), the function to integrate
def f(x):
    return x*math.sin(x**2)

#defines the limts for the function
(a,b)=(0,math.sqrt(math.pi))
#(a,b)=(input("Lower limit? "),input("Upper limit? "))
#print("The limits are ("+str(a)+","+str(b)+")")

#asks user for # of steps to compute
steps=int(input("How many steps? "))
print("The steps are "+str(steps)+"")
print("Calculating...")

#start of program
tstart=time.time()

#calculates the width of each step
dx=(b-a)/steps
#print("deltax="+deltax+"")

#add y0 to area
x=a
Area=f(x)
#make x = x1
x=x+dx

#computes yx and adds it to total area, starting with x1 and adding dx each time to ensure the next loop runs with x2, x3, xn-1 and so on
while x < b:
    Area=Area+2*f(x)
    x=x+dx

#computes final area by multipling by (dx/2) after adding yn to area
Areaf=(dx/2)*(Area+f(b))

tend = time.time()
telapsed = tend - tstart
print("The estimated integral is "+str(Areaf)+" using "+str(steps)+" steps.")
print("The time elasped was "+str(telapsed)+" seconds.")
