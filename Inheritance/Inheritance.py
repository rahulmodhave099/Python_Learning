
# Inheritance

# all classes have parent class "object" automatically.
class Company(object):
    x = 10

    def __init__(self,cmpName,loc):
        self.cmpName = cmpName
        self.loc = loc

    def compInfo(self):
        print(self.cmpName)
        print(self.loc)

class Employee(Company):
    pass

obj1 = Company("Microsoft","Pune")
obj2 = Company("Microsoft","Bangalore")

obj1.compInfo()

obj3 = Employee("Microsoft","Pune")
obj4 = Employee("Microsoft","Bangalore")

obj3.compInfo()
obj4.compInfo()