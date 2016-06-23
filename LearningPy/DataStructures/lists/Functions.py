'''
Created on Jan 12, 2016

@author: gaiyamperumal
'''
# Built in Functions and lists
lotto = [2, 14, 26, 62, 41, 20]
print len(lotto)
print max(lotto)
print min(lotto)
print sum(lotto)
print sum(lotto)/len(lotto)


# List Methods [append, count, extend, index, insert, pop, remove, reverse, sort]
# Build list with append
stuff = list()
stuff.append('Book')
stuff.append(99)
print stuff
stuff.append('cookie')
print stuff

# In a list?
some = [0, 2, 5, 8, 14, 19]
print 8 in some
print 10 in some
print 20 not in some 

# List is an ordered sequence 
friends = ['Paul', 'Richard', 'Koteeswaran']
friends.sort()
print friends
friends.reverse()
print friends