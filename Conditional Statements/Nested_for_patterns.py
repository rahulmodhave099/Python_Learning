'''
* * *
* * *
* * *
'''
for i in range(3):
    for j in range(3):
        print(end="* ")
    print()

'''
1 2 3
1 2 3
1 2 3
'''
for i in range(3):
    num = 1
    for j in range(3):
        print(num,end=" ")
        num += 1
    print()

'''
1 2 3
2 3 4
3 4 5
'''
for i in range(3):
    for j in range(3):
        print(i+j+1,end=" ")
    print()

# OR
for i in range(3):
    num = i + 1
    for j in range(3):
        print(num,end=" ")
        num += 1
    print()

'''
1 2 3
2 4 6
3 6 9
'''
for i in range(3):
    num = i + 1
    for j in range(3):
        print(num,end=" ")
        num += i+1
    print()
# OR
for i in range(3):
    num = i + 1
    for j in range(3):
        print(end=" ")
    print()


'''
*
* *
* * *
'''
for i in range(3):
    for j in range(i+1):
        print("*",end=" ")
    print()

'''
1
2 3
4 5 6
'''
num = 1
for i in range(3):
    for j in range(i+1):
        print(end="%d "%num)
        num += 1
    print()

'''
A 
B C
D E F
'''
num = 65
for i in range(3):
    for j in range(i+1):
        print(chr(num),end=" ")
        num += 1
    print()

# NOTE : here we used chr() in built function to convert numbers into character by their ascii values

'''
1 2 3
4 5
6
'''
num = 1
for i in range(3):
    for j in range(3-i):
        print(num,end=" ")
        num += 1
    print()

