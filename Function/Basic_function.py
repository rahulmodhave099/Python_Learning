
def sumTwo(a,b):
    print("In fun")
    ans = a + b
    print(ans)

x = int(input("Enter value for x : "))
y = int(input("Enter value for y : "))

sumTwo(x,y)
sumTwo(x+10,y+20)


def sumN(a):
    add = 0
    for i in range(1,a+1):
        add += i
    print(add)

x = int(input("Enter value for x : "))
sumN(x)


def div(a):
    if(a%4 == 0 and a%5 == 0):
        print("%d is Divisible by both 4 & 5"%a)
    else:
        print("%d is not Divisible by both 4 & 5"%a)


x = int(input("Enter value for x : "))

div(x)


def playerinfo(num,name):
    print("{} : {}.".format(name,num))

jersyNo = int(input("Enter Jersy Number : "))
pName = input("Enter Player Name : ")

playerinfo(jersyNo,pName)


