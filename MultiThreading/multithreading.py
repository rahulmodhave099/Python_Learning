# /usr/lib/python3.12/threading.py  at this locations python modules are stored

# Thread class from module threading

import threading,os
#from threading import Thread
'''
# Single thread : MainThread

print("Start Code")

def fun():
    print("In fun")

print(threading.current_thread().name)                  # MainThread

fun()

for x in range(1,11):
    print(x)

print(os.getpid())

print(threading.current_thread().name)

# Method 1 : Multiple Threads

def fun(x,y):
    print("In fun function")
    print(threading.current_thread().name)
    print(x,y)
    for i in range(6):
        print("In fun")

def mun():
    print("In mun function")
    print(threading.current_thread().name)
    for i in range(6):
        print("In mun")

print(threading.current_thread().name)

thread1 = threading.Thread(target = fun,args=[10,20])
thread2 = threading.Thread(target = mun)

thread1.start()
thread2.start()

# Method 2 : Multiple Threads using class

#class MyThread(Thread):
#        OR
class MyThread(threading.Thread):

    def __init__(self,x,y):
        threading.Thread.__init__(self)
        self.x = x
        self.y = y

    def run(self):
        print("In run method",self.x,self.y)
        print(threading.current_thread().name)
        #      OR
        #print(threading.current_thread().getName())

print(threading.current_thread().name)

t1 = MyThread(10,20)
t1.start()
'''
# Method 3 : Multiple Threads using class

class MyThread():

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def display(self):
        print("In run method",self.x,self.y)
        print(threading.current_thread().name)

print(threading.current_thread().name)

obj = MyThread(10,20)
t1 = threading.Thread(target = obj.display)
t1.start()
