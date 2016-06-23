'''
Created on Dec 23, 2015

@author: gaiyamperumal

Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
Award time-and-a-half for the hourly rate for all hours worked above 40 hours. 
Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. 
The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use raw_input to read a string and float() to convert the string to a number. 
Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
'''
def computepay(h,r):
    p = h*r
    return p

try:
    inp = raw_input("Enter Hours:")
    hrs = float(inp)
    inp = raw_input("Enter Rate:")
    rate = float(inp)
except:
    print "Enter a valid numeric values"

if hrs > 40:
    ehrs = hrs - 40
    pay = computepay(40,rate) + computepay(ehrs,(rate*1.5))
else:
    pay = computepay(hrs,rate)

print pay