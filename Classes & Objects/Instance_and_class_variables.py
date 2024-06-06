# Constructor and Instance Variable

'''
Constructor :
In Python , Constructor is defined by the dunder method (double underscore method) __init__(self) ,
as it is used to initialize variables of the class.
As object is created, instantly constructor gets automatically called and the code inside constructor gets initialize.
The variables inside the constructor are called as instance variables and the methods which use self as argument
are instance methods.
As Objects are created , then they stores the variables and methods from the class and we can access them using object.
Self contains the address of the object and by passing self as a parameter to the methods inside class ,
methods get access to instance variables.
Such methods are called as Instance methods.
'''
# Instance Variables
class Employee:

    def __init__(self, empId=0, empName=None):
        print("In Constructor")
        self.empId = empId
        self.empName = empName

    def empInfo(self):
        print(self.empId)
        print(self.empName)


emp1 = Employee(12, "Kanha")
emp2 = Employee(15, "Ashish")
emp3 = Employee()

emp1.empInfo()
emp2.empInfo()
emp3.empInfo()

emp1.empId = 50
emp1.empName = "Badhe"

emp1.empInfo()

# class variables / Static variables

'''
The variables which are present inside the class instead of initializing in constructor or inside a method ,
such variables are called as "class or static variables". 
The class variable is present in class namespace and also present a copy into class objects.
Thus we can access the class variable by class name as well as by class object.
We have given it in below example :  

'''

class Company:
    cmpName = "Facebook"

    def __init__(self):
        print("In Constructor")
        self.empId = 12
        self.empName = "Kanha"

    def compInfo(self):
        print(self.empId)
        print(self.empName)
        print(self.cmpName)
        print(Company.cmpName)

emp1 = Company()

emp1.compInfo()


class Organisation:
    cmpName = "Facebook"

    def __init__(self):
        print("In Constructor")

    def compInfo(self):
        print(self.cmpName)

emp1 = Organisation()
emp2 = Organisation()

print(Organisation.cmpName)                     # Facebook
emp1.compInfo()                                 # Facebook
emp2.compInfo()                                 # Facebook

emp1.cmpName = "Meta"

print(Organisation.cmpName)                     # Facebook
emp1.compInfo()                                 # Meta
emp2.compInfo()                                 # Facebook

Organisation.cmpName = "Meta"

print(Organisation.cmpName)                     # Meta
emp1.compInfo()                                 # Meta
emp2.compInfo()                                 # Meta
