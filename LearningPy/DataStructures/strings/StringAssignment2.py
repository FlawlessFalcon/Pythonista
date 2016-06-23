'''
Created on Jan 11, 2016

@author: gaiyamperumal

Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output 
as shown below. You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter 
mbox-short.txt as the file name.

'''
fname = raw_input('Enter the file name:')
try:
    fhand = open(fname)
except:
    print 'Invalid file name.'
    exit()
value = 0
count = 0
for line in fhand:
    line = line.rstrip()
    if not 'X-DSPAM-Confidence:' in line:
        continue
    else:
        count = count + 1
        pos = line.find(':')
        value = value + float(line[pos+1:].strip())
        ave = value/count
print ave

