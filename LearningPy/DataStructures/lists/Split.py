'''
Created on Jan 12, 2016

@author: gaiyamperumal
'''
# String and Lists
abc = 'hello world'
stuff = abc.split()
print stuff

line = 'hello;world;check;this'
thing = line.split(';')
print thing

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print words[2]

t = [9, 41, 12, 3, 74, 15]
print t[2:4]