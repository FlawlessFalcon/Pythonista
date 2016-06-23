'''
Created on Jan 15, 2016

@author: gaiyamperumal

Words - the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car
'''
counts = dict()
line = raw_input('Enter a line of text: ')
words = line.split()
print 'Words:', words
print 'Counting...'
for word in words:
    counts[word] = counts.get(word, 0) + 1
print 'Counts', counts 