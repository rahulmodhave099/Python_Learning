# syntax error
'''
def fun()
    print("Hello")

fun()

# Indentation Error

def fun():
    print("Hello")
        print("Hello")

fun()

# type error  : it occurres when it deos not match with the given entity.

def fun(a,b):
    print(a)
    print(b)

print("Start Code")
fun(10,20)
fun(10)
print("End Code")

# OR

def fun(a, b):
    print(a+b)

fun(10,"Rahul")
print("End Code")

# Attribute error : it occurres when it deos not find any entity/method to access inside class.

class Demo:

    def fun(self):
        print("In Fun")

Demo().gun()

 # Name error  : it occurres when it deos not find any entity/method to access outside class/global space.

class Demo:

    def fun(self):
        print("In Fun")

fun()
'''

# Attribute error for NoneType
class Demo:

    def fun(self):
        print("In Fun")

    def gun(self):
        print("In Fun")

obj = Demo()
obj.fun()

obj = None
obj.gun()

# Index error  : out of bound index

list1 = [10,20,30,40]

print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])

# key error

players = {18:"Virat",45:"Rohit",7:"MSD"}

print(players[45])
print(players[18])
print(players[1])



