'''
Created on Jan 15, 2016

@author: gaiyamperumal
'''
counts = dict()
names = ['jil', 'jung', 'chuck', 'kurivi', 'shoot', 'jil', 'jung', 'chuck', 'jil', 'jil']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print counts
print counts.get('jil', 0)
        