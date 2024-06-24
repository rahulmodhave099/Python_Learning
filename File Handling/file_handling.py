# File Handling
# 2 types of files
# 1. Text files : txt,pdf
# 2. binary files : jpg,mp3,mp4

# Opening and closing a file
# open("filename","filemode")   where filemode is task/reason of file for opening e.g read,write
'''
fileobj = open("core2web.txt")

print(type(fileobj))

# reading from a file

fileobj = open("core2web.txt","r")

print(fileobj.read())

f = open("incubator.txt","r")

print(f.read())
print(f.read())

f.seek(0)

print(f.read())
'''

# reading and writing into a file

f1 = open("core2web.txt","r+")

print(f1.readable())
print("###################################################")

# 3 types of reading files : read,readline,readlines

print(f1.tell())
print("###################################################")

print(f1.read())
print("###################################################")

print(f1.tell())
print("###################################################")

f1.seek(0)

print(f1.readline())
print("###################################################")

f1.seek(0)
print(f1.readlines())
