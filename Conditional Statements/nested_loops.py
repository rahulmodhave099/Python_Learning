
for i in range(1,5):
    print("*",end=" ")

print()

for i in range(4):
    print(i+1,end=" ")

print()

for i in range(2,15,2):
    print(i,end=" ")

print()

for i in range(1,10,2):
    print(i,"*",end=" ")

print()

for i in range(1,11):
    if(i%2 == 1):
        print(i,end=" ")
    else:
        print("*",end=" ")

print()

for i in range(1,51):
    if(i%5 == 0 and i%2 == 1):
        print(i,end=" ")
    elif(i%5 == 0 and i%2 == 0):
        print("*",end=" ")

print()

for i in range(5,51,5):
    if(i%2 == 0):
        print("*",end=" ")
    else:
        print(i,end=" ")
print()

for i in range(1,20):
    if(i%3 == 0):
        print("Three")
    elif(i%5 == 0):
        print("Five")
    else:
        print(i)
print()

# Nested For loop

for i in range(3):
    print("In i for loop")
    for j in range(3):
        print("In j for loop")

print()

for i in range(3):
    print("In i for loop")
    for j in range(i):
        print("In j for loop")

print()

for i in range(3):
    print("In i for loop")
    for j in range(i+1):
        print("In j for loop")

print()

for i in range(3):
    for j in range(3):
        print("*",end=" ")

print()

for i in range(3):
    for j in range(3):
        print("*",end=" ")
    print()

print()

for i in range(3):
    for j in range(3):
        print("*",end=" ")
        print()

print()

num = 1

for i in range(3):
    for j in range(3):
        print(num,end=" ")
        num += 1
    print()

print()

for i in range(3):
    for j in range(3):
        print(i+1,end=" ")
    print()

print()

# OR

num = 1

for i in range(3):
    for j in range(3):
        print(num,end=" ")
    num += 1
    print()

print()


for i in range(3):
    for j in range(3):
        print(j+1,end=" ")
    print()

print()

# OR

for i in range(3):
    num = 1
    for j in range(3):
        print(num,end=" ")
        num += 1
    print()

print()

