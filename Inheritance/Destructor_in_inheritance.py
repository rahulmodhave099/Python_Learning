'''
class Parent:
    p = 30
    def __init__(self):
        print("In Parent Constructor")
        self.x = 10
        self.y = 20

    def dispData(self):
        print(self.x)
        print(self.y)

    @classmethod
    def dispParent(cls):
        print(cls.p)

class Child(Parent):
    pass

print(Parent.p)
obj = Child()
print(obj.dispData)
obj.dispData()

Parent.dispParent()
'''

# Destructor

class Parent:
    p = 30
    def __init__(self):
        print("In Parent Constructor")
        self.x = 10
        self.y = 20

    def dispData(self):
        print(self.x)
        print(self.y)

    def __del__(self):
        print("In destructor")

obj = Parent()
obj.dispData()
#obj.__del__()
del obj
print("#############################################")
# For 2 different objects
#obj1 = Parent()
#obj2 = Parent()
print("#############################################")

# For 2 objects having same name

obj3 = Parent()
obj3 = Parent()
print("Code samplay")
