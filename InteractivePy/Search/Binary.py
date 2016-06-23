# coding=utf-8
'''
It is possible to take greater advantage of the ordered list if we are clever with our comparisons
In the sequential search, when we compare against the first item, there are at most n−1 more items to look through if the first
item is not what we are looking for
Instead of searching the list in sequence, a binary search will start by examining the middle item.
If that item is the one we are searching for, we are done. If it is not the correct item, we can use the ordered nature of the list to eliminate
half of the remaining items

Analysis of Binary Search:
Comparisons	Approximate Number of Items Left
1	n/2
2	n/4
3	n/8
...
i	n/2^i

The number of comparisons necessary to get to this point is i where n/2^i=1. Solving for i gives us i=logn.

Therefore, the binary search is O(logn)O(log⁡n)
'''

__author__="Ganesh"

# Binary Search of an Ordered List of Integers
# This algorithm is a great example of a divide and conquer strategy


def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))



# Recursive version of Binary Search

def binarySearchRecursive(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearchRecursive(alist[:midpoint],item)
            else:
                return binarySearchRecursive(alist[midpoint+1:],item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearchRecursive(testlist, 3))
print(binarySearchRecursive(testlist, 13))