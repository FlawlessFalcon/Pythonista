__author__="Ganesh"


print(type("Hello, World!"))
print(type(17))
print("Hello, World")
print(type(3.2))
print(type("17"))
print(type("3.2"))
print(type('This is a string.') )
print(type("And so is this.") )
print(type("""and this.""") )
print(type('''and even this...''') )
print('''"Oh no", she exclaimed, "Ben's bike is broken!"''')

message = """This message will
span several
lines."""
print(message)

print("""This message will span
several lines
of the text.""")

print('This is a string.')
print("""And so is this.""")

print(42000)
print(42,000)

print(42, 17, 56, 34, 11, 4.35, 32)
print(3.4, "hello", 45)

print(3.14, int(3.14))
print(3.9999, int(3.9999))       # This doesn't round to the closest int!
print(3.0,int(3.0))
print(-3.999,int(-3.999))        # Note that the result is closer to zero

print("2345",int("2345"))        # parse a string to produce an int
print(17,int(17))                # int even works on integers
print(int("23"))

print(float("123.45"))
print(type(float("123.45")))

print(str(17))
print(str(123.456))
print(type(str(123.456)))