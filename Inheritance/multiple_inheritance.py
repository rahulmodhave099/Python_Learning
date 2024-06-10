# Multiple inheritance
# MRO : Method Resolution order

class Parent1:

    def __init__(self):
        print("In Constructor : Parent 1")

    def dispData(self):
        print("In dispData")

class Parent2:

    def __init__(self):
        print("In Constructor : Parent 2")

    def printData(self):
        print("In printData")

class Child(Parent2,Parent1):
    '''
    def __init__(self):
        print("In Constructor : Child")
    '''

obj = Child()                       # Here left thumb rule(DFS) is applied for which constructor is to be get called
obj = Child()                       # Here left thumb rule() is applied for which constructor is to be get called
                                    # from parent constructors.
                                    # It runs constructor of the parent class which is present first
                                    # i.e. present at left side first
obj.dispData()
obj.printData()

class A:

    def fun(self):
        print("In fun : A")

class B:

    def fun(self):
        print("In fun : B")


class C:

    def fun(self):
        print("In fun : C")


class D(A,B):

    def fun(self):
        print("In fun : D")
        super().fun()


class E(B, C):

    def fun(self):
        print("In fun : E")
        super().fun()


class F(D, E):

    def fun(self):
        print("In fun : F")
        super().fun()

obj = F()
obj.fun()

print(F.mro())