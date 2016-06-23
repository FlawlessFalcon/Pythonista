'''
Created on Dec 23, 2015

@author: gaiyamperumal
'''
largest_so_far = -1
print 'Before', largest_so_far
for num in [9,41,3,12,74,15]:
    if num > largest_so_far:
        largest_so_far = num
    print largest_so_far, num
print 'After', largest_so_far
