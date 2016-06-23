'''
less than	<	Less than operator
greater than	>	Greater than operator
less than or equal	<=	Less than or equal to operator
greater than or equal	>=	Greater than or equal to operator
equal	==	Equality operator
not equal	!=	Not equal operator
logical and	and	Both operands True for result to be True
logical or	or	One or the other operand is True for the result to be True
logical not	not	Negates the truth value, False becomes True, True becomes False

'''
__author__ = "Ganesh"

print(5==10)
print(10 > 5)
print((5 >= 1) and (5 <= 10))

myList = [1,2,3,4]
A = [myList]*3
print(A)
myList[2]=45
print(A)