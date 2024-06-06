class Company:
    def disp(self):
        print("Hello")


obj = Company()

print("Start Code")
obj.disp()
print(type(obj))
print("End Code")


# Constructor

'''
Constructor :
In Python , Constructor is defined by the dunder method (double underscore method) __init__(self) ,
as it is used to initialize variables of the class.
As object is created, instantly constructor gets automatically called and the code inside constructor gets initialize.
The variables inside the constructor are called as instance variables and the methods which use self as argument 
are instance methods.

'''
class Employee:
    def __init__(self):
        print("In Constructor")
        self.x = 10
        self.y = 20

    def disp(self):
        print(self.x)
        print(self.y)

obj = Employee()


