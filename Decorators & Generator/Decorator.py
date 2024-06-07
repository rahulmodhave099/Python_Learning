# Function Decorator

def run():
    print("In run")

def fun(x):
    print("In fun")
    x()

fun(run)
#fun(run())

def gun():
    print("In gun")

def run(y):
    print("In run")
    y()


def fun(x):
    print("In fun")
    x()

fun(run(gun))

def decorFun(func):

    def wrapper():
        print("Enter the wrapper")
        func()
        print("End of wrapper")

    return wrapper
@decorFun
def normalFun():
    print("In Normal Function")

#normalFun = decorFun(normalFun)
normalFun()


def decorFun(func):
    print("In DecorFun")
    def wrapper(*args):
        print("In Wrapper")
        val = func(*args)
        print("End Wrapper")
        return val

    return wrapper
@decorFun
def normalFun(*args):
    print("In normalFun")
    sum = 0
    for i in args:
        sum += i
    return sum

#print(decorFun(normalFun(10,20,30)))

#normalFun = decorFun(normalFun,10,20)

print(normalFun(10,20))

# Decorator Chaining

def decorFun(func):

    def wrapper():
        print("Enter the wrapper 2")
        func()
        print("End of wrapper 2")

    return wrapper

def decorRun(func):

    def wrapper():
        print("Enter the wrapper 1")
        func()
        print("End of wrapper 1")

    return wrapper
@decorFun
@decorRun
def normalFun():
    print("In Normal Function")

#normalFun = decorFun(decorRun(normalFun))
normalFun()