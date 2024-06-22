# syntax error

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

# Attribute error : it occurres when it deos not find any entity/method in class.

class Demo:

    def fun(self):
        print("In Fun")

Demo().gun()

 # Name error  : it occurres when it deos not find any entity/method in outside class/global space.

class Demo:

    def fun(self):
        print("In Fun")

fun()

