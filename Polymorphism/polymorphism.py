class Demo:

    def fun(self):
        print("In Demo : fun")


class Memo:

    def gun(self):
        print("In Memo : fun")


def callFun(obj):
    if(id(obj) == id(obj1)):
        obj.fun()
    else:
        obj.gun()


obj1 = Demo()
obj2 = Memo()

callFun(obj2)