# Polymorphism
# Polymorphism is a method of having different characteristic at the same time which changes according to condition.

class Demo:

    def fun(self):
        print("In Demo : fun")

class Memo:

    def gun(self):
        print("In Memo : gun")

def callFun(obj):
    if(obj == obj1):
        obj.fun()
    elif(obj == obj2):
        obj.gun()
    #  OR
    if(obj is Demo):
        obj.fun()
    elif(obj is Memo):
        obj.gun()
    #  OR
    if (id(obj) == id(obj1)):
        obj.fun()
    elif(id(obj) == id(obj2)):
        obj.gun()
    # OR
    if hasattr(obj,'fun'):
        obj.fun()
    elif hasattr(obj,'gun'):
        obj.gun()

obj1 = Demo()
obj2 = Memo()

callFun(obj1)
callFun(obj2)

#  Another example

y = "Rahul"
z = ["Core2web","Rahul","Modhave"]

print(len(y))
print(len(z))


# operator overloading

# example 1
a = 10
b = 20

print(a + b)

c = "Rahul"
d = "_Modhave"

print(c + d)

# example 2
class Demo:
    x = 10

    def __eq__(self,obj):
        print("I am here")
        return id(self) == id(obj)

class Memo:
    x = 20

obj1 = Demo()
obj2 = Memo()

print(obj1 == obj2)

# example 3

x = 20
y = 10.5

print(x + y)
