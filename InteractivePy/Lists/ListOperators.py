# coding=utf-8
'''
When pop is called on the end of the list it takes O(1) but when pop is called on the first element in the list or anywhere in the middle
it is O(n). The reason for this lies in how Python chooses to implement lists. When an item is taken from the front of the list,
in Python’s implementation, all the other elements in the list are shifted one position closer to the beginning.

Operation	    Big-O Efficiency
index []	        O(1)
index assignment	O(1)
append	            O(1)
pop()	            O(1)
pop(i)	            O(n)
insert(i,item)	    O(n)
del operator	    O(n)
iteration	        O(n)
contains (in)	    O(n)
get slice [x:y]	    O(k)
del slice	        O(n)
set slice	        O(n+k)
reverse	            O(n)
concatenate	        O(k)
sort	            O(n log n)
multiply	        O(nk)

'''
__author__="Ganesh"

import timeit

x = list(range(2000000))

popzero = timeit.Timer("x.pop(0)",
                       "from __main__ import x")
popend = timeit.Timer("x.pop()",
                      "from __main__ import x")

print popzero.timeit(number=1000)
print popend.timeit(number=1000)

print("pop(0)   pop()")
for i in range(1000000,100000001,1000000):
    x = list(range(i))
    pt = popend.timeit(number=1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print("%15.5f, %15.5f" %(pz,pt))