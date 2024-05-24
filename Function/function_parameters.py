def fun(x:int,y:int)->int:
    print(x)
    print(y)
    return "hello"

a = fun(50,60)
b = fun("sachin","shashi")

print(a)
print(b)


# Default Parameter

def add(x,y,z=30):
    print(x)
    print(y)
    print(z)

add(10,20)
add(10,20,44)

'''
def add(x=50,y,z=30):
    print(x)
    print(y)
    print(z)

add(10,20)

line 26
    def add(x=50,y,z=30):
                 ^
SyntaxError: parameter without a default follows parameter with a default
'''

#Named Argument / Name Parameter

def compInfo(cname,empCount):
    print(cname," : ",empCount)

compInfo("Microsoft",70000)
compInfo("Amazon",50000)
compInfo("Apple",30000)

compInfo(10000,"Google")

compInfo(empCount=10000,cname="Google")

# Passing Variable number of arguments to a function
# Var args (various arguments)

def fun1(*argv):
    for i in argv:
        print(i)

fun1(10,20,30,40)

def fun2(x,y,*argv):
    print(x)
    print(y)
    print(argv)

fun2(10,20,30,40)

def fun3(x,y,*argv):
    print(x)
    print(y)
    print(argv)

fun3(10,20)

'''
def fun4(*argv,x,y):
    print(x)
    print(y)
    print(argv)

fun4(10,20)

It Gives error because argv takes all values in its tuple and x and y parameters missing their values
line 78, in <module>
    fun4(10,20)
TypeError: fun4() missing 2 required keyword-only arguments: 'x' and 'y'
'''

# Key-Word Arguments
# Passing variable number of Key-Word Arguments to a function

def fun5(**argv):
    print(argv)
    print(type(argv))


fun5(x=10,y=20,z=30)

'''
def fun6(**argv,x,z):
    print(argv)
    print(type(argv))


fun6(x=10,y=20,z=30)

Gives Error
line 97
    def fun6(**argv,x,z):
                    ^
SyntaxError: arguments cannot follow var-keyword argument
'''

def fun6(x,z,**argv):
    print(argv)
    print(type(argv))


fun6(x=10,y=20,z=30)

def fun7(**argv):
    print(argv)
    print(type(argv))
    for key,value in argv.items():
        print(key,":",value)


fun7(x=10,y=20,z=30)

# Above code runs successfully bcoz '**argv' takes all the remainig arguments
# thus it should return as a last parameter of function OR it should be given single parameter




