'''
Created on Dec 18, 2015

@author: gaiyamperumal
Rewrite the below program with try except so that your program handles non numeric entry gracefully.
Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use raw_input to read a string and float() to convert the string to a number. 
Do not worry about error checking the user input - assume the user types numbers properly.
'''
inp = raw_input("Enter Hours: ")
try:
    hours = float(inp)
    inp = raw_input("Enter Rate: ")
    try:
        rate = float(inp)
        pay = hours * rate
        print pay
    except: 
        print "Enter a numeric value"
except:
    print "Enter a numeric value"
    

