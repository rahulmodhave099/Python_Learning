import array_slicing as arr
# import array
# from array import *

jersyno = arr.array('i',[45,77,18,96,1])

print(jersyno)
print(type(jersyno))

for ele in jersyno:
    print(ele)

'''
jersyno = array
arr = module
array = function
i = typecode(datatype of array)
[] = data collection(multiple element)

typecode                size
b/B(byte)               1
u(string)               4
h/H(short integer)      2
i/I(integer)            4
l/L(long integer)       8
q/Q(long long integer)  8
f(float)                4
d(double)               8
'''

data = arr.array('b',[10,20,30,40,50])

print(data.itemsize)        #Gives size of the type of data(typecode)

# Character Array

name = arr.array('u',['R','o','h','i','t'])

print(name)             #array('u', 'Rohit')

#NOTE : Python deos not support string array thus python have List data type for string array like ["Rohit","Virat"]



