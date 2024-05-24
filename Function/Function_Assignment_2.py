def fun():
    print("in fun")
if __name__ == "__main__" :
    fun()
'''
Explanation:
1. def fun(): ...: This defines a function named fun that simply prints the message
"in fun" when called.
2. if _name_ == "_main_": ...: This conditional statement checks whether the
code is being executed directly (as the main program) or if it is being imported as
a module into another program.
● When a Python code is executed, the _name_ variable is set to
"_main_" if it is the entry point of the program.
● If the code is imported as a module into another code, the _name_
variable is set to the name of the module, not "_main_".
3. fun(): If the program is being run as the main program (i.e., _name_ is
"_main_"), it calls the fun function, resulting in the message "in fun" being
printed.
Write the following code given below and perform a dry run
for the provided codes.
'''
#Code 1:
def add(x):
    def inner(y):
        return x + y
    return inner

if __name__== '__main__':
    add_3 = add(3)
    result = add_3(7)
    print(result)

#Output: 10


#Code 2:
def outer():
    def inner():
        return "Greetings from the inner function!"
    return inner()

if __name__=="__main__":
    result = outer()
    print(result)

#Output: Greetings from the inner function!

#Code 3:
def outer():
    def inner():
        return "This is the inner function."
    return inner

if __name__=="__main__":
    retObj = outer()
    retInner = retObj()

    print(retInner)

#output: This is the inner function.

#Code 4:
def outer():
    def inner():
        return outer
    return inner

if __name__=="__main__":
    retObj = outer()
    retInner = retObj()
    print(retInner)

#Output: address of outer function

#Code 5:
def outer():
    def inner(outer):
        print(outer)
        return inner

    return inner(outer)

if __name__=="__main__":
    retObj = outer()
    print(retObj)

#Output: address of outer fun
#        address of inner fun


#Code 6:
def outer():
    def inner1(a, b):
        print("In inner1")
        return a - b

    def inner2(obj):
        print("In inner2")
        print(obj)
        return inner2

    retInner1 = inner1(10, 4)
    retInner2 = inner2(retInner1)
    return retInner2

if __name__=="__main__":
    retObj = outer()
    print(retObj)

#Output: In inner1
#        In inner2
#        6
#        address of inner()

#Code 7:
def outer():
    def inner():
        return "Hello, Core2web!"

    return inner
    print("In Outer Function")

if __name__=="__main__":
    result = outer()()
    print(result)

#Output: Hello, Core2web!

#Code 8:
def outer():
    message = "I am the outer function."

    def inner():
        return message

    return inner

if __name__=="__main__":
    inner_function = outer()
    result = inner_function()
    print(result)

#Output: I am the outer function.

#Code 9:
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner

if __name__=="__main__":
    counter = outer()
    print(counter())
    print(counter())

#Output:?

#Code 10:
def outer(flag):
    def inner():
        return "This is true." if flag else "This is false."

    return inner

if __name__=="__main__":
    true_function = outer(True)
    false_function = outer(False)

    print(true_function())
    print(false_function())

#Output:



