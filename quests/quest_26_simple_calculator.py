#!/usr/bin/python3
x=int(input("enter the first number: "))
y=int(input("enter the second number: "))
operation=input("enter the operation: ")
def add(x,y):
     return x+y
def subtract(x,y):
    return x-y
def divide(x,y):
    if y==0: 
        print("the denominator is zero i.e error ")
    else:
        return x/y
def multiply(x,y):
    return x*y

if operation=="add":
    print("sum: " ,add(x,y))
elif operation=="subtract":
    print("difference: " ,subtract(x,y))
elif operation=="multiply":
    print("product :",multiply(x,y))
elif operation=="divide":
    print("quotient: ",divide(x,y))
else: print("This is a simple calculator,put one of the four main operations")
