# coding=utf-8
'''

The order of magnitude function describes the part of T(n) that increases the fastest as the value of n increases.
Order of magnitude is often called Big-O notation (for “order”) and written as O(f(n)).

As another example, suppose that for some algorithm, the exact number of steps is T(n)=5n2+27n+1005T(n)=5n2+27n+1005. When n is small, say 1 or 2,
the constant 1005 seems to be the dominant part of the function. However, as n gets larger, the n2n2 term becomes the most important. In fact,
when n is really large, the other two terms become insignificant in the role that they play in determining the final result. Again, to approximate
T(n)T(n) as n gets large, we can ignore the other terms and focus on 5n25n2. In addition, the coefficient 55 becomes insignificant as n gets large.
We would say then that the function T(n)T(n) has an order of magnitude f(n)=n2f(n)=n2, or simply that it is O(n2)O(n2).

f(n)	    Name
1	    Constant
logn	Logarithmic
n	    Linear
nlogn	Log Linear
n^2	    Quadratic
n^3	    Cubic
2^n	    Exponential

'''

__author__="Ganesh"

# Order of n^2

test = 0
for i in range(n):
   for j in range(n):
      test = test + i * j

# Order of n

test = 0
for i in range(n):
   test = test + 1

for j in range(n):
   test = test - 1

# Order of log n

i = n
while i > 0:
   k = 2 + 2
   i = i // 2

a=5
b=6
c=10
n = input('Please enter the value of n: ')
for i in range(n):
   for j in range(n):
      x = i * i
      y = j * j
      z = i * j
for k in range(n):
   w = a*k + 45
   v = b*b
d = 33


