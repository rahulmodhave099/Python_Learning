class Demo:

    z = 30                              # public

    def __init__(self):
        self._x = 10                    # protected
        self.__y = 20                   # private : can be access outside class by _Demo__y

    def __fun(self):
        print("In private fun")

print(dir(Demo))

obj = Demo()

print(dir(obj))

print(obj.z)
print(obj._x)
#print(obj.__y)                         # error at this line  AttributeError: 'Demo' object has no attribute '__y'
print(obj._Demo__y)

obj._Demo__fun()