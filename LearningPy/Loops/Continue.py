'''
Created on Dec 23, 2015

@author: gaiyamperumal
'''
while True:
    line = raw_input('Enter details: ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print line
print 'Done'