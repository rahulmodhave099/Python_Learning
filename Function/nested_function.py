
def outer():

    def inner1():
        print("In Inner1 Function")
    '''
    inner2()
    Above line gives error bcoz inner2() fun is gets called before declaring the function
    UnboundLocalError: cannot access local variable 'inner2' where it is not associated with a value
    '''
    def inner2():
        print("In Inner2 function")

    print("In Outer Function")
    inner1()
    inner2()
'''
inner1()
Above line gives error bcoz inner1() fun is inside the outer() fun ,
and it cannot get called be outside inner function  ,it need to be get called inside outer() fun
NameError: name 'inner1' is not defined
'''
outer()

# Function Returning Function

def outer(x,y):

    def inner(a,b):
        print("In Inner Function")
        return a+b

    print("In Outer Function")
    print(x+y)
    return inner

retObj = outer(10,20)
innerRet = retObj(3,4)
print(type(retObj))
print(retObj)

def outer():

    def inner1():
        print("In inner1 function")
    def inner2():
        print("In inner2 function")

    return inner1,inner2

retobj = outer()
print(retobj)
for i in retobj:
    print(i)

for i in retobj:
    i()

def outer():

    def inner1(a,b):
        print("In inner1 function")
        return a+b
    def inner2(x,y):
        print("In inner2 function")
        return x*y

    return inner1,inner2

retObj = outer()

inn1 , inn2 = retObj

ret1 = inn1(10,20)
ret2 = inn2(3,4)

print(ret1+ret2)

print(inn1)
print(inn2)

def outer():

    def inner1():
        print("Inner1")

    return inner1
    print("In Outer")

retobj = outer()
retobj()