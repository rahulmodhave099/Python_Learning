# Multiple inheritance
# MRO : Method Resolution order

class Parent1:

    def dispData(self):
        print("In dispData")

class Parent2:

    def printData(self):
        print("In printData")

class Child(Parent2,Parent1):
    pass

obj = Child()                       # here left thumb rule is applied for which constructor is to be get called
                                    # it runs constructor of the parent class which is present first
                                    # i.e. present at left side first
obj.dispData()
obj.printData()