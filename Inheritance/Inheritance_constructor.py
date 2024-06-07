class Demo:
    def __init__(self):
        print("in constructor")
        self.x = 10
        self.y = 20

    def setData(self,z):
        self.z = z


    def printData(self):
        print(self.x)
        print(self.y)
        #print(self.z)

obj = Demo()

obj.printData()

# Constructor in inheritance

class Parent:
    def __init__(self):
        print("Parent Constructor 1")

    def __init__(self):
        print("Parent Constructor 2")

    def printData(self):
        print("In Fun 1")

    def printData(self):
        print("In Fun 2")

obj1 = Parent()
obj1.printData()

class Parent:

    def __init__(self):
        print("In Parent constructor")

    def parentFun(self):
        print("In parent function")

class Child(Parent):

    def __init__(self):
        # If we want to call both constructor i.e. parent also we have below method
        #Parent()                           By creating object for parent class we can call parent constructor
        #              OR
        #super().__init__()
        #              OR
        Parent.__init__(self)
        print("In Child Constructor")

    def childFun(self):
        print("In child fun")

obj1 = Parent()
obj1.parentFun()

obj2 = Child()
obj2.parentFun()
obj2.childFun()

