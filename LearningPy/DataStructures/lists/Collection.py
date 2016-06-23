'''
Created on Jan 12, 2016

@author: gaiyamperumal
'''
# A lists is a kind of Collection
friends = ['Joseph', 'Sally' , 'Glenn']

# Not a collection [simple variable]
x = 2 
x = 4 
print x

#List Constants 
print [1, 43, 23]
print ['Joseph', 'Sally']
print ['red', 24, 98.6]
print [1, [5, 6], 7]
print []

for i in [1, 2, 3, 4, 5]:
    print i
print 'Blast Off'

# Lists and Definite LOOPS

friends = ['Paul', 'Richard', 'Koteeswaran']
for friend in friends:
    print 'Happy New Year', friend
print 'Bye Bye !!!'

# Looking inside Lists

friends = ['Paul', 'Richard', 'Koteeswaran'] # [0-Paul, 1-Richard, 2-Koteeswaran]
print friends[1]

# Lists are mutable String are not 'We cannot change any letter in string 'Banana''
lotto = [2, 14, 26, 62, 41, 20]
print lotto
lotto[0] = 9
lotto[5] = 90
print lotto
print len(lotto)
print range(len(lotto))

# Range 
friends = ['Paul', 'Richard', 'Koteeswaran']
for i in range(len(friends)):
    friend = friends[i]
    print 'Happy New Year', friend
print 'Bye Bye !!!'

#Concatenate lists

a = [1, 2, 3]
b = [3, 4, 5, 6]
print a+b

# List slicing

print b[1:3]
print b[:7]
print b[2:]
print b[:]

#Averaging with a list
numlist = list()
while True:
    inp = raw_input('Enter valid numbers')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
    
average = sum(numlist)/len(numlist)
print average 


    