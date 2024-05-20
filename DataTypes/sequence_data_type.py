# Sequence Data Type

# 1. String        <class 'str'>
#method - 1

friend1 = "Kanha"
print(friend1)
print(type(friend1))

#method - 2

friend2 = 'Ashish'
print(friend2)
print(type(friend2))

#method - 3

friend3 = '''Rahul'''
print(friend3)
print(type(friend3))

#method - 4

friend4 = """Shashi"""
print(friend4)
print(type(friend4))

# 2. List        <class 'list'>

empList = [18,"Ashish",25.5,45,"kanha",35.5]
print(empList)
print(type(empList))

empList[4] = "Rahul"
print(empList)

# 3. Tuple        <class 'tuple'>

empTuple = (18,"Ashish",25.5,45,"kanha",35.5)
print(empTuple)
print(type(empTuple))

#empTuple[4] = "Rahul"          gives error on this line
print(empTuple)


# 4. Range          <class 'range'>

x=range(10)
y=range(21,41)

print(x)
print(type(x))

for i in x:
    print(i)

print(y)
print(type(y))

for j in y:
    print(j)

