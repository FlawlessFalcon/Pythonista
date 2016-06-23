'''
center	astring.center(w)	Returns a string centered in a field of size w
count	astring.count(item)	Returns the number of occurrences of item in the string
ljust	astring.ljust(w)	Returns a string left-justified in a field of size w
lower	astring.lower()	Returns a string in all lowercase
rjust	astring.rjust(w)	Returns a string right-justified in a field of size w
find	astring.find(item)	Returns the index of the first occurrence of item
split	astring.split(schar)	Splits a string into substrings at schar

A major difference between lists and strings is that lists can be modified while strings cannot. This is referred to as mutability.
Lists are mutable; strings are immutable. For example, you can change an item in a list by using indexing and assignment.
With a string that change is not allowed
'''

__author__ = "Ganesh"

myName = "David"
print myName[3]
print myName*2
print len(myName)
print myName.upper()
print myName.center(10)
print myName.find('v')
print myName.split('v')
