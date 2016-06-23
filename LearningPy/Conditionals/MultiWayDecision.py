'''
Created on Dec 23, 2015

@author: gaiyamperumal
'''
x = raw_input('Enter a number: ')

if x < 2:
    print 'Small'
elif x < 10:
    print 'Medium'
elif x < 20:
    print 'Big'
elif x < 40:
    print 'Large'
elif x < 100:
    print 'Huge'
else:
    print 'Ginormous'
print 'All done'
    