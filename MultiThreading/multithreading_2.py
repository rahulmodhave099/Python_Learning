import threading
from threading import Thread

print("Start Code")

print(threading.current_thread())       # thread_name   and  id
print(threading.current_thread().name)       # thread_name
print(threading.current_thread().ident)       # id
