import threading
from threading import Thread

'''
print("Start Code")

print(threading.current_thread())       # thread_name   and  id
print(threading.current_thread().name)       # thread_name
print(threading.current_thread().ident)       # id  

class MyThread(Thread):

        def run(self):
            print("In run")
            print(threading.current_thread().name)


print(threading.current_thread().name+" Start")
t1 = MyThread()
t1.start()

print(threading.current_thread().name+" End")

'''

class Demo:

    def dispInfo(self):
        print("In dispInfo")
        print(threading.current_thread().name)

    def dispData(self):
        print("In dispData")
        print(threading.current_thread().name)

print("MainThread")
obj = Demo()

t1 = Thread(target = obj.dispInfo)
t2 = Thread(target = obj.dispData)

t1.start()
t2.start()

print("MainThread End")
