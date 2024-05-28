# set

setdata1 = {}

print(setdata1)
print(type(setdata1))               # <class 'dict'>

setdata2 = set()

print(setdata2)
print(type(setdata2))               # <class 'set'>

setdata3 = {1,2,3,4,5}
print(setdata3)                     # {1,2,3,4,5}

setdata4 = {1,"A",10.5,True}         # It does not print "True" value from the set.
# bcoz set deos not print duplicate data where set already includes 1 as True is considered as 1.
print(setdata4)                     # {1,'A',10.5}

setdata5 = {1,"A",10.5,0,True,False}     # Sequence changed one time. It does not print "True" and "False" both values from Set.
# bcoz set deos not print duplicate data where set already includes 1 and 0 as True and False are considered as 1 and 0.
print(setdata5)                     # {0,1,10.5,'A'}

setdata6 = {"Ashish","Kanha","Badhe","Rahul"}           # For this o/p sequence changes everytime
print(setdata6)                     # {'Kanha', 'Badhe', 'Ashish', 'Rahul'}

setdata7 = {"A",10.5,True,False,1,0}
print(setdata7)                             # {False, True, 10.5, 'A'}

setdata8 = set([10,20,30,40])
print(setdata8)

setdata9 = set("Rahul")
print(setdata9)

# setdata10 = set(10)
# print(setdata10)                       TypeError: 'int' object is not iterable

# access and add

set = {1,2,3,4,5}

# print(set[2])                         TypeError: 'set' object is not subscriptable

print(set)

# set[2] = 50                             TypeError: 'set' object does not support item assignment

print(set)

set.add(6)

print(set)

# frozenset

set2 = frozenset([1,2,3,4,5])
print(set2)
# set2.add(6)                       AttributeError: 'frozenset' object has no attribute 'add'

print(set2)


