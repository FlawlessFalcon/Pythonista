'''
Created on Jan 11, 2016

@author: gaiyamperumal
'''
#Count
fHand = open('JMeter.txt')
count = 0
for line in fHand:
    count = count +1
print 'Line Count:', count

#Read & Length
fHand1 = open('JMeter.txt')
inp = fHand1.read()
print len(inp)

#Print specific lines

fHand2 = open('JMeter.txt')
for line in fHand2:
    line = line.rstrip() #To removed unvanted lines
    if line.startswith('1.'):
        print line

# Skip uninterested line        
fHand3 = open('JMeter.txt')
for line in fHand3:
    line = line.rstrip()
    # Skip Uninteresting line 
    if not line.startswith('1.'):
        continue
    # Process interesting Line
    print line

#prompt file name
fname = raw_input('Enter The File Name:')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('1.'):
        count = count + 1
print 'There were', count, '1. lines in', fname


