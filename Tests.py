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


n = int(input("What n? "))
a0 = int(input("starting value for a0? "))
an = a0
counter = 1
while counter <= n:
    an = math.sqrt(2+math.sqrt(an))
    print (an)
    counter = counter+1
print("The final number is "+str(an)+"!")