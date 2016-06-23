# coding=utf-8

'''
d, i	Integer
u	Unsigned integer
f	Floating point as m.ddddd
e	Floating point as m.ddddde+/-xx
E	Floating point as m.dddddE+/-xx
g	Use %e for exponents less than −4−4 or greater than +5+5, otherwise use %f
c	Single character
s	String, or any Python data object that can be converted to a string by using the str function.
%	Insert a literal % character

number	%20d	Put the value in a field width of 20
-	%-20d	Put the value in a field 20 characters wide, left-justified
+	%+20d	Put the value in a field 20 characters wide, right-justified
0	%020d	Put the value in a field 20 characters wide, fill in with leading zeros.
.	%20.2f	Put the value in a field 20 characters wide with 2 characters to the right of the decimal point.
(name)	%(name)d	Get the value from the supplied dictionary using name as the key.

'''

__author__="Ganesh"

aName = input('Please enter your name: ')
age = input('Please enter your age: ')
print("Hello")
print("Hello","World")
print("Hello","World", sep = "***")
print("Hello","World", end = "***")

print(aName, "is", age, "years old.")
print("%s is %d years old." % (aName, age))

price = 24
item = "banana"
print("The %s costs %d cents"%(item,price))
print("The %+10s costs %5.2f cents"%(item,price))
print("The %+10s costs %10.2f cents"%(item,price))
itemdict = {"item":"banana","cost":24}
print("The %(item)s costs %(cost)7.1f cents"%itemdict)
