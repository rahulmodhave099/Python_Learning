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

