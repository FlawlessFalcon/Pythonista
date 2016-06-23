'''
Created on Dec 23, 2015

@author: gaiyamperumal
'''
#String Data Type
str1 = 'Hello'
str2 = 'there'
bob = str1 + str2
print bob
str3 = 123
str4 = str3 + 1 # Fails as String cannot be added to int

x = int(str3) + 1
print x

#Looking Inside Strings
fruit = 'banana' #[0]=b, [1]=a so on
letter = fruit[0]
print letter

#Length function
print len(fruit)

#Looping through strings
index = 0
while index < len(fruit):
    letter = fruit[index]
    print index, letter
    index = index + 1
    
for letter in fruit:
    print letter 

# Looping and Counting
count = 0
for letter in fruit:
    if letter == 'a':
        count = count + 1
    print count 
    
# Slicing String
s = 'Monty Python'
print s[0:4]
print s[6:20]
print s[:2]
print s[8:]
print s[:]

#Using in Operator
print 'n' in fruit
print 'm' in fruit
print 'nan' in fruit 
if 'a' in fruit:
    print 'Found it!'

#String Library
greet = 'Hello Bob'
zap = greet.lower()
print zap
print zap.upper()

#Search a String
pos = fruit.find('na')
print pos

#Replace
rep = greet.replace('Bob', 'Jane')
print rep
print rep.replace('e', 'E')

#Strip Whitespace
rock = ' Hello Guys '
print rock.strip()

#Prefixes
#print fruit starts_with('b')
print greet.find('l')
    