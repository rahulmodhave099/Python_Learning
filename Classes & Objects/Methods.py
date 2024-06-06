# Methods types

# 1. Instance Method 2. class methods 3. static methods

# Instance Methods

'''
Constructor is gets automatically called when the objects created from class.
Instance Methods can access instance variable using "self" keyword.
Self keyword contains address of objects as they gets passed to the methods as a parameter while creating object.
Thus we can use self keyword to access both instance variables and instance methods.
Self contains the address of the object and by passing self as a parameter to the methods inside class ,
methods get access to instance variables.
Such methods are called as Instance methods.
As object is created, instantly constructor gets automatically called and the code inside constructor gets initialize.
The variables inside the constructor are called as instance variables and the methods which use self as argument
are instance methods.
As Objects are created , then they stores the variables and methods from the class and we can access them using object.
In below example , instance method playerInfo() has given self as a parameter ,
so it have the address where variable and methods are stored .
'''

class Player:
    teamName = "India"

    def __init__(self,jerNo,pName):
        print("In Constructor")
        self.jerNo = jerNo
        self.pName = pName

    def playerInfo(self):
        print(self.jerNo)
        print(self.pName)
        print(self.teamName)

cric1 = Player(18,"Virat")
cric2 = Player(45,"Rohit")

cric1.playerInfo()
cric2.playerInfo()


# 2. class method

'''
The method which is directly connected to the class is called as class method. 
It is denoted by "@classmethod" while defining the method.
Class method takes the parameter "cls" which stores address of class itself.
In class method, using cls we can access the class variables but we cannot able to access the instance variable 
bcoz class dont have the address of objects where the instance variables has been stored.
Thus in class methods we can access only class variables. 
But objects have the copy of class variables so objects can access class methods and variables.
Class method is present in class namespace , So We can call the class method by both class as well as class object.
Below check in example :  
'''

class Player:
    teamName = "India"

    def __init__(self,jerNo,pName):
        print("In Constructor")
        self.jerNo = jerNo
        self.pName = pName

    @classmethod
    def playerInfo(cls):
        print(cls.teamName)


cric1 = Player(18,"Virat")
cric2 = Player(45,"Rohit")

Player.playerInfo()
cric1.playerInfo()

# 3. static method

'''
It is denoted by "@staticmethod" while defining the method.
Static method is not belong to class or either object , thus it does not take any parameter.
Static Method access only class variables by class name. 
As it deos not take any parameter i.e. self or cls so it does not have access to instance variable or object variables
but it have only access to class variable by using class name.  
Static method is present in class namespace so it can be accessible by both class and class object. 
But it is not related to class or class object.
'''

class Player:
    teamName = "India"

    def __init__(self,jerNo,pName):
        print("In Constructor")
        self.jerNo = jerNo
        self.pName = pName

    @staticmethod
    def playerInfo():
        print(Player.teamName)


cric1 = Player(18,"Virat")
cric2 = Player(45,"Rohit")

Player.playerInfo()
cric1.playerInfo()