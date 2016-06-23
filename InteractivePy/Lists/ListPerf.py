'''
Two common operations are indexing and assigning to an index position. Both of these operations take the same amount of time no matter
how large the list becomes. When an operation like this is independent of the size of the list they are O(1).

Another very common programming task is to grow a list. You can use the append method or the concatenation operator. The append method is O(1).
However, the concatenation operator is O(k) where k is the size of the list that is being concatenated

'''

__author__ = "Ganesh"

import timeit

# Generate a list of n numbers starting with 0
# Concat
def listN1():
    l = []
    for i in range(1000):
        l = l + [i]


# Append
def listN2():
    l = []
    for i in range(1000):
        l.append(i)


# Comprehension
def listN3():
    l = [i for i in range(1000)]


# List Range
def listN4():
    l = list(range(1000))


t1 = timeit.Timer("listN1()", "from __main__ import listN1")
print("concat ", t1.timeit(number=1000), "milliseconds")
t2 = timeit.Timer("listN2()", "from __main__ import listN2")
print("append ", t2.timeit(number=1000), "milliseconds")
t3 = timeit.Timer("listN3()", "from __main__ import listN3")
print("comprehension ", t3.timeit(number=1000), "milliseconds")
t4 = timeit.Timer("listN4()", "from __main__ import listN4")
print("list range ", t4.timeit(number=1000), "milliseconds")
