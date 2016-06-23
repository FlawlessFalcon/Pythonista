'''
Created on Dec 23, 2015

@author: gaiyamperumal
Write a program which reads list of numbers until 'done' is entered. Once 'done' is entered print out the total, count and average of the 
numbers. If the user enter other than numbers print an error message and skip to the next number.
'''
count = 0
total = 0
while True:
    inp = raw_input('Enter valid numbers: ')
    if inp == 'done': break
    try:
        num = float(inp)
    except:
        print "Enter a valid numeric number"
        continue
    count = count + 1
    total = total + num
    print count, total
print 'Average', total / count 
