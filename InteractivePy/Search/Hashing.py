# coding=utf-8
'''

The concept of building a data structure that can be searched in O(1) time is referred to as hashing.
A hash table is a collection of items which are stored in such a way as to make it easy to find them later.
Each position of the hash table, often called a slot, can hold an item and is named by an integer value starting at 0
Initially, the hash table contains no items so every slot is empty.
The mapping between an item and the slot where that item belongs in the hash table is called the hash function
The hash function will take any item in the collection and return an integer in the range of slot names, between 0 and m-1

Simple Hash Function Using Remainders
Item	Hash Value
54	    10
26	    4
93	    5
17	    6
77	    0
31	    9
Once the hash values have been computed, we can insert each item into the hash table at the designated position as shown in Figure 5.
Note that 6 of the 11 slots are now occupied. This is referred to as the load factor, and is commonly denoted by λ=numberofitem/stablesize.
For this example, λ=6/11

Simple Hash Function Using Folding Method
If our item was the phone number 436-555-4601, we would take the digits and divide them into groups of 2 (43,65,55,46,01). After the addition,
43+65+55+46+0143+65+55+46+01, we get 210. If we assume our hash table has 11 slots, then we need to perform the extra step of dividing by 11
and keeping the remainder. In this case 210 % 11 is 1, so the phone number 436-555-4601 hashes to slot 1. Some folding methods go one step
further and reverse every other piece before the addition. For the above example, we get 43+56+55+64+01=21943+56+55+64+01=219 which gives
219 % 11=10

Simple Hash Function Using Mid-square method
If the item were 44, we would first compute 442=1,936442=1,936. By extracting the middle two digits, 93, and performing the remainder step,
we get 5 (93 % 11)

Comparison of Remainder and Mid-Square Methods
Item	Remainder	Mid-Square
54	    10	        3
26	    4	        7
93	    5	        9
17	    6	        8
77	    0	        4
31	    9	        6
'''

__author__="Ganesh"

# Remainder Method (modulo arithmetic) (h(item)=item%11)
# Collision - In hash function if two or more items need to be in the same slot
# Given a collection of items, a hash function that maps each item into a unique slot is referred to as a perfect hash function

# Folding Method - constructing hash functions begins by dividing the item into equal-size pieces (the last piece may not be of equal size).
# These pieces are then added together to give the resulting hash value

# Numerical technique for constructing a hash function is called the mid-square method
# We first square the item, and then extract some portion of the resulting digits

# String Hash functions
# The word “cat” can be thought of as a sequence of ordinal values.
# We can then take these three ordinal values, add them up, and use the remainder method to get a hash value
print ord('c')
print ord('a')
print ord('t')

def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])
        print sum

    return sum%tablesize

# Hashing a String Using Ordinal Values with Weighting useful for anagram 

def hashPos(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])*(pos+1)
        print sum

    return sum%tablesize

print hash("cat",11)
print hashPos("cat", 11)