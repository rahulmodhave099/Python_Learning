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


class Parent:
    x = 10
    y = 20

    @classmethod
    def dispData(cls):
        print("Parent method")
        print(cls.x)
        print(cls.y)

class Child(Parent):

    x = 30
    y = 40

    @classmethod
    def dispData(cls):
        print("Child method")
        super().dispData()
        print(cls.x)
        print(cls.y)

obj = Child()
obj.dispData()