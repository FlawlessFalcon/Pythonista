'''
Dictionaries are collections of associated pairs of items where each pair consists of a key and a value. This key-value pair is typically written
as key:value. Dictionaries are written as comma-delimited key:value pairs enclosed in curly braces.

[]	myDict[k]	Returns the value associated with k, otherwise its an error
in	key in adict	Returns True if key is in the dictionary, False otherwise
del	del adict[key]	Removes the entry from the dictionary

keys	adict.keys()	Returns the keys of the dictionary in a dict_keys object
values	adict.values()	Returns the values of the dictionary in a dict_values object
items	adict.items()	Returns the key-value pairs in a dict_items object
get	adict.get(k)	Returns the value associated with k, None otherwise
get	adict.get(k,alt)	Returns the value associated with k, alt otherwise

'''

__author__ = "Ganesh"

capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print capitals
print(capitals['Iowa'])
capitals['Utah']='SaltLakeCity'
print(capitals)
capitals['California']='Sacramento'
print(len(capitals))
for k in capitals:
   print(capitals[k]," is the capital of ", k)


phoneext={'david':1410,'brad':1137}
print phoneext
print phoneext.keys()
print list(phoneext.keys())
print phoneext.values()
print list(phoneext.values())
print phoneext.items()
print list(phoneext.items())
print phoneext.get("kent")
