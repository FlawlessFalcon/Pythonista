'''
Created on Jan 12, 2016

@author: gaiyamperumal

Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() function. 
The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it 
to the list. When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.pythonlearn.com/code/romeo.txt
'''
fname = raw_input('Enter the file name:')
try:
    fhand = open(fname)
except:
    print 'Invalid file name.'
    exit()
romeolist = list()
count = 0
for line in fhand:
    word = line.rstrip().split()
    for element in word:
        if element in romeolist:
            continue
        else:
            romeolist.append(element)
print sorted(romeolist)