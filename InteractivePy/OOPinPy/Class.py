'''
1. We define a new class by providing a name and a set of method definitions that are syntactically similar to function definitions.
2. The constructor method is always called _init_ (two underscores before and after init)
3. 'self' is a special parameter that will always be used as a reference back to the object itself.
    It must always be the first formal parameter; however, it will never be given an actual parameter value upon invocation

'''

_author_="Ganesh"

class Fraction:

    def _init_(self,top,bottom):

        self.num = top
        self.den = bottom

    def show(self):
        # type: () -> object
        print(self.num, "/", self.den)

    def _str_(self):
        return str(self.num) + "/" + str(self.den)

myfraction = Fraction(3,5)
print myfraction

f1 = Fraction(1,4)
f2 = Fraction(1,2)
print f1.add_(f2)
