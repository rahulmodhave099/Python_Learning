# /user/lib/python3.12/threading.py  at this locations python modules are stored

import threading

print("Start Code")

def fun():
    print("In fun")

print(threading.current_thread().name)

fun()