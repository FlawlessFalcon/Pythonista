'''
Created on Dec 23, 2015

@author: gaiyamperumal
'''

# Sequential
name = raw_input('Enter File:')
handle = open(name, 'r')
text = handle.read()
words = text.split()
counts = dict()

#Repeated
for word in words:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None

for word,count in counts.items():
    
    #Conditional
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print bigcount, bigword