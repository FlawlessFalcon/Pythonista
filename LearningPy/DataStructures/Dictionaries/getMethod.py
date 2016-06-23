'''
Created on Jan 15, 2016

@author: gaiyamperumal
'''
#if name in counts:
#   print counts['name']
#else:
#    print 0

counts = dict()
print counts.get('name', 0)

counts = dict()
names = ['jil', 'jung', 'chuck', 'kurivi', 'shoot', 'jil', 'jung', 'chuck', 'jil', 'jil']
for name in names:
        counts[name] = counts.get(name, 0) + 1
print counts
print counts.get('jil', 0)