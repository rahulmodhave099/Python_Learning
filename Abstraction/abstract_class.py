from abc import *

class Demo(ABC):

    def __init__(self):
        print("Constructor Demo")

    @abstractmethod
    def fun(self):
        print("In fun method")

#Demo()         #TypeError: Can't instantiate abstract class Demo without an implementation for abstract method 'fun'

class Hyundai(metaclass=ABCMeta):

    def slogun(self):
        print("New Thinking , New Possibilities")

    @abstractmethod
    def carType(self):
        pass

class Verna(Hyundai):

    def carType(self):
        print("Sedan")


class Creta(Hyundai):

    def carType(self):
        print("SUV")

obj1 = Verna()
obj1.slogun()
obj1.carType()

obj2 = Creta()
obj2.slogun()
obj2.carType()

print(Creta.__mro__)





