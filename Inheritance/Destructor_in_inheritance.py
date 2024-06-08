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

class Parent1:
    def __init__(self):
        print("In parent Constructor")
        self.x = 10
        self.y = 20

    def dispParent(self):
        print(self.x)
        print(self.y)

class Child(Parent1):

    def __init__(self):
        print("In child Constructor")
        # super().__init__()
        self.x = 30
        self.y = 40
        super().__init__()

    def dispChild(self):
        print(self.x)
        print(self.y)

obj = Child()
obj.dispParent()
obj.dispChild()
'''

class Parent:
    x = 10
    y = 20

    @classmethod
    def dispData(cls):
        print(cls.x)
        print(cls.y)

class Child(Parent):

    x = 30
    y = 40

    @classmethod
    def dispData(cls):
        print(cls.x)
        print(cls.y)
        super().dispData()