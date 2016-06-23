'''
Created on May 5, 2016

@author: gaiyamperumal
'''
def count_words(input, n):
    words = str.split(input ) 
# create simple dictionary of words and how many times it occurred in the string 
    d = dict()
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    print d
    for w in sorted(d, key=d.get, reverse=True):
        print w, d[w]

count_words("betty a bought a bit of butter but the butter was bitter bitter bitter", 4)