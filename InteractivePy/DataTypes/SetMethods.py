'''
membership	in	Set membership
length	len	Returns the cardinality of the set
|	aset | otherset	Returns a new set with all elements from both sets
&	aset & otherset	Returns a new set with only those elements common to both sets
-	aset - otherset	Returns a new set with all items from the first set not in second
<=	aset <= otherset	Asks whether all elements of the first set are in the second

union	aset.union(otherset)	Returns a new set with all elements from both sets
intersection	aset.intersection(otherset)	Returns a new set with only those elements common to both sets
difference	aset.difference(otherset)	Returns a new set with all items from first set not in second
issubset	aset.issubset(otherset)	Asks whether all elements of one set are in the other
add	aset.add(item)	Adds item to the set
remove	aset.remove(item)	Removes item from the set
pop	aset.pop()	Removes an arbitrary element from the set
clear	aset.clear()	Removes all elements from the set

'''
__author__="Ganesh"

mySet = {3,6,"cat",4.5,False}
print mySet
print len(mySet)
print False in mySet
print "dog" in mySet
yourSet = {99,3,100}
print mySet.union(yourSet)
print mySet | yourSet
print mySet.intersection(yourSet)
print mySet & yourSet
print mySet.difference(yourSet)
print mySet - yourSet
print {3,100}.issubset(yourSet)
print {3,100}<=yourSet
print mySet.add("house")
print mySet.remove(4.5)
print mySet.pop()
print mySet
mySet.clear()
print mySet
