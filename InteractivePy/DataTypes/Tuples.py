'''
Tuples are very similar to lists in that they are heterogeneous sequences of data. The difference is that a tuple is immutable, like a string.
A tuple cannot be changed. Tuples are written as comma-delimited values enclosed in parentheses. As sequences, they can use any operation
described above

'''

__author__ = "Ganesh"

myTuple = (2,True,4.96)
print myTuple
print len(myTuple)
print myTuple[0]
print myTuple * 3
print myTuple[0:2]
myTuple[0:2]

myTuple[1]=False