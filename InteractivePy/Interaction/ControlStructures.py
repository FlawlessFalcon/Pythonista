'''
Algorithms require two important control structures: iteration and selection
Python provides a standard while statement and a very powerful for statement
While statement repeats a body of code as long as a condition is true
    The while statement is a very general purpose iterative structure that we will use in a number of different algorithms.
    In many cases, a compound condition will control the iteration
For statement can be used to iterate over the members of a collection, so long as the collection is a sequence

'''

__author__="Ganesh"

# While statement repeats a body of code as long as a condition is true

counter = 1
while counter <= 5:
    print ("Hello World")
    counter = counter + 1

# while counter <= 10 and not done:
# The value of the variable counter would need to be less than or equal to 10 and the value of the variable done would need to be False
    # (not False is True) so that True and True results in True



# Works for any collection that is a sequence (lists, tuples, and strings)
for item in [1,3,5,7,9]:
    print item

for item in range(5):
    print item**2

wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
print(letterlist)