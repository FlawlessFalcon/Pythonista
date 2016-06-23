'''
Created on Dec 22, 2015

@author: gaiyamperumal

Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, 
print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except 
and put out an appropriate message and ignore the number.
'''

largest = None
smallest = None
num = None
while True:
    inp = raw_input("Enter a valid number: ")  
    if inp == "done": break 
    try:
        num = int(inp)
        if largest is None and smallest is None:
            largest = num
            smallest = num
        elif num > largest:
            largest = num
        elif num < smallest:
            smallest = num   
    except:
        print "Enter a valid numeric number"
print "Maximum is ", largest
print "Minimum is ", smallest
