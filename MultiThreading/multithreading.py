# /usr/lib/python3.12/threading.py  at this locations python modules are stored

import threading,os
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
'''
# Multiple Threads

def fun():
    print("In fun function")
    print(threading.current_thread().name)
    for i in range(6):
        print("In fun")

def mun():
    print("In mun function")
    print(threading.current_thread().name)
    for i in range(6):
        print("In mun")

print(threading.current_thread().name)

thread1 = threading.Thread(target = fun)
thread2 = threading.Thread(target = mun)

thread1.start()
thread2.start()
