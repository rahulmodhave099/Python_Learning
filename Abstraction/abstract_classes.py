# Abstract classes

from program import ICC

class BCCI(ICC):

    def __init__(self):
        print("In constructor BCCI")

class IPL(BCCI):

    def __init__(self):
        print("In constructor IPL")

print(IPL.__mro__)

if __name__ == '__main__':
    IPL()
else:
    BCCI()