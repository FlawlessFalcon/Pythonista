'''
Created on Dec 23, 2015

@author: gaiyamperumal
'''
smallest_so_far = None
print 'Before', smallest_so_far
for num in [9,41,3,12,74,15]:
    if smallest_so_far is None:
        smallest_so_far = num
    elif num < smallest_so_far:
        smallest_so_far = num
    print smallest_so_far, num
print 'After', smallest_so_far