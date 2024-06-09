class Demo:

    z = 30

    def __init__(self):
        self._x = 10
        self.__y = 20


print(dir(Demo))

obj = Demo()

print(dir(obj))

print(obj.z)
print(obj._x)
#print(obj.__y)
print(obj._Demo__y)