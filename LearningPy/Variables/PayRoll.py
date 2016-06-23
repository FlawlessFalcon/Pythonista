'''
Created on Dec 18, 2015

@author: gaiyamperumal
Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. Use 35 hours and a rate of 2.75 per 
hour to test the program (the pay should be 96.25). You should use raw_input to read a string and float() to convert the string to a number. 
Do not worry about error checking or bad user data.
'''
inp = raw_input("Enter Hours: ")
hours = float(inp)
inp = raw_input("Enter Rate: ")
rate = float(inp)
pay = hours * rate
print "Pay", pay

