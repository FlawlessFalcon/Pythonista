# coding=utf-8

'''
Algorithm Analysis
An interesting question often arises. When two programs solve the same problem but look different, is one program better than the other?

'''

__author__="Ganesh"

def sumOfN(n):
   theSum = 0
   for i in range(1,n+1):
       theSum = theSum + i

   return theSum

print(sumOfN(10))

# Poor Coding for Sum of N integers

def foo(tom):
    fred = 0
    for bill in range(1,tom+1):
       barney = bill
       fred = fred + barney

    return fred

print(foo(10))


#Execution of time for the Function

import time

def sumOfN2(n):
   start = time.time()

   theSum = 0
   for i in range(1,n+1):
      theSum = theSum + i

   end = time.time()

   return theSum,end-start

print(sumOfN2(10))

for i in range(5):
    print("Sum is %d required %10.7f seconds" % sumOfN2(10000))
    print("Sum is %d required %10.7f seconds" % sumOfN2(100000))
    print("Sum is %d required %10.7f seconds" % sumOfN2(1000000))

# takes advantage of a closed equation ∑ni=1i=(n)(n+1)2∑i=1ni=(n)(n+1)2 to compute the sum of the first n integers without iterating.

def sumOfN3(n):
    sum = 0
    start = time.time()
    sum = (n*(n+1))/2
    end = time.time()
    return sum, end-start

print("Sum is %d required %10.8f seconds" % sumOfN3(10000))
print("Sum is %d required %10.8f seconds" % sumOfN3(100000))
print("Sum is %d required %10.8f seconds" % sumOfN3(1000000))