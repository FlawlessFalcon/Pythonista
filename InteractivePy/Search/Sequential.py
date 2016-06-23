'''
When data items are stored in a collection such as a list, we say that they have a linear or sequential relationship
In Python lists, these relative positions are the index values of the individual items
Since these index values are ordered, it is possible for us to visit them in sequence
This process gives rise to our first searching technique, the sequential search.

'''

__author__="Ganesh"

def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))

# What would happen to the sequential search if the items were ordered in some way? Would we be able to gain any efficiency in our search technique?
# Assume that the list of items was constructed so that the items were in ascending order, from low to high.

def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos+1

    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(orderedSequentialSearch(testlist, 3))
print(orderedSequentialSearch(testlist, 13))
