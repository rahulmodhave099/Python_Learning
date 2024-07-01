# daemon thread : Daemon keyword is used to set lowest priority to the thread.
# It has boolean values . If daemon = True then this thread has lowest priority & thus main thread can skip
# the daemon thread output if daemon thread getting too much time to run OR having complexity while running.
# If daemon thread is not complex and not taking too much time to run then daemon thread can also work.

# In below example we have written thread-1 as daemon thread and it has given sleep period of 10 sec.
# As main thread completes his work and he waits until thread-2 completes his work and then terminate the code.
# MainThread deos not wait for thread-1 because it has low priority.

# But if we do not give sleep to thread-2 , then the possibility of skipping daemon thread is depend upon their
# complexity & required timr.

import threading
from threading import Thread
import time


class Demo:

    def fun(self):
        time.sleep(5)
        print("In fun")
        print(threading.current_thread().name )

    def gun(self):
        time.sleep(3)
        print("In gun")
        print(threading.current_thread().name)

print("Start MainThread")

obj = Demo()

t1 = Thread(target = obj.fun,daemon = True)
t2 = Thread(target = obj.gun)

t1.start()
t2.start()

print("End MainThread")
