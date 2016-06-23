'''
Created on May 5, 2016

@author: gaiyamperumal
'''
import collections 
 
def count_words(input, n):
    words = str.split(input ) 
# create simple dictionary of words and how many times it occurred in the string 
    d = dict()
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
   
# sort the dictionary by value in descending order
    d_ordered = collections.OrderedDict()
    
    for key, value in sorted(d.iteritems(), key=lambda (k,v):(v,k), reverse=True):
        print"%s: %s" % (key, value)
        d_ordered[key] = value
    
# in case of tie sort the tied words alphabetically
    last_value = 0
    temp_dict = collections.OrderedDict()
    final_dict = collections.OrderedDict()
 
    for key, value in sorted(d_ordered.iteritems(), key=lambda (k,v): (v, k), reverse=True):
 
        if (last_value == 0):
            temp_dict[key] = value
            last_value = value
        elif (value == last_value):
            temp_dict[key] = value
            last_value = value
        elif (value != last_value):
            for k, v in sorted(temp_dict.iteritems()):
                print"adding to final %s: %s" % (k, v)
                final_dict[k] = v
            print(sorted(temp_dict.iteritems()))
            print("count inside temp_dict before clear ", len(temp_dict))
            temp_dict.clear()
            print("count inside temp_dict ", len(temp_dict))
            temp_dict[key] = value
            last_value = value
        
    print(sorted(temp_dict.iteritems()))
    for k, v in sorted(temp_dict.iteritems()):
        print"Individually adding  %s: %s" % (k, v)
        final_dict[k] = v
       # final_dict.update(sorted(temp_dict.iteritems()))
 
# Grab the top n as list from the final ordered dictionary
    top_n = []
    for item in final_dict.items():
       if (n > 0):
           top_n.append(item)
           n = n - 1
           print"adding to top_n %s: %s" % item
       if (n == 0):
           break
 
    return top_n  
 
print count_words("betty a bought a bit of butter but the butter was bitter bitter bitter", 4)