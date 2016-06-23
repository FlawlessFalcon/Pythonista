'''
Created on Jan 15, 2016

@author: gaiyamperumal
Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python 
dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, 
the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

fname = raw_input('Enter the file name:')
try:
    fhand = open(fname)
except:
    print 'Invalid file name.'
    exit()
counts = dict()
for line in fhand:
    words = line.rstrip().split()
    print 'Words:', words
    print 'Counting...'
    for word in words:
        if not line.startswith('From '):
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
print 'Counts', counts 